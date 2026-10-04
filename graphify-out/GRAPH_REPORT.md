# Graph Report - jak-project  (2026-10-04)

## Corpus Check
- Large corpus: 1536 files · ~2,430,782 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder.

## Summary
- 35271 nodes · 76260 edges · 972 communities (889 shown, 83 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 8323 edges (avg confidence: 0.84)
- Token cost: 1,431,386 input · 0 output

## Community Hubs (Navigation)
- Renderer Bucket IDs
- GOAL Compiler Core
- Game Kernel Runtime
- Overlord ISO and IOP
- x86 Emitter and Codegen
- mips2c Execution Context
- Tfrag3 and TIE Data
- Compiler IR and Regalloc
- Decompiler Utilities
- Listener and Sockets
- DMA Follower and Sprite3
- MIPS Instruction Set
- Compiler Test Runner
- Compiler Environments
- Decompiler Form Matching
- Decompiler Atomic Ops
- Overlord Jak X Streams
- GS Registers and Depth Cue
- LSP Handlers
- Compiler Values and Regs
- Decompiler IR2 Env
- Generic2 Renderer
- Overlord Jak 2 Buffers
- Sound Player RPC
- Form Expression Analysis
- Overlord Jak 1 ISO Queue
- Overlord Jak 3 Streams
- Decompiler Form Elements
- Kernel Memory and DGO Link
- Kernel Print and Call GOAL
- Level Extractor Shrub
- Compiler Static Data
- Texture Animator
- Overlord Jak 2 Streams
- Offline Test Orchestration
- Tie3 and Tfrag Renderer
- Data Decompile and TypeSpec
- mips2c TIE Methods
- ARM64 Emitter Tests
- GOOS Interpreter
- game/graphics: BucketRenderer
- goalc/compiler: IR.cpp
- game/sce: iop.cpp
- decompiler/analysis: AtomicOp
- decompiler/level_extractor: string
- game/graphics: TFragment
- game/graphics: OpenGLRenderer
- common/goos: Object
- decompiler/level_extractor: extract_merc.cpp
- goalc/build_actor: jak1/build_actor.cpp
- game/kernel: common/kmachine.cpp
- goalc/build_actor: jak3/build_actor.cpp
- decompiler/level_extractor: extract_tie.cpp
- common/type_system: type_system/Type.cpp
- decompiler/IR2: bitfields.cpp
- decompiler/IR2: Kind
- decompiler/Disasm: TEST()
- goalc/emitter: ObjectGenerator.cpp
- test/goalc: TEST_F()
- goalc/build_actor: jak2/build_actor.cpp
- game/kernel: jak2/kscheme.cpp
- goalc/compiler: throw_compiler_error()
- decompiler/level_extractor: GameVersion
- game/kernel: cprintf()
- game/kernel: jak3/kscheme.cpp
- game/overlord: GetThreadId()
- game/graphics: DirectRenderer2
- game/graphics: AdgifHelper
- decompiler/Function: Function
- decompiler/analysis: analyze_inspect_method.c
- game/kernel: jakx/kscheme.cpp
- decompiler/IR2: StaticInfo
- goalc/build_level: Region
- goalc/build_level: Region
- game/system: mutex
- decompiler/ObjectFile: ObjectFileDB
- decompiler/level_extractor: extract_tfrag.cpp
- goalc/compiler: TypeDocumentation
- goalc/regalloc: TEST()
- test/decompiler: FormRegressionTest.cpp
- decompiler/VuDisasm: VuInstrK
- game/common: Vf
- test/goalc: test_vector_float.cpp
- game/system: InputBindingGroups
- common/dma: DrawMode
- game/mips2c: get_fake_spad_addr2()
- decompiler/level_extractor: Level
- game/overlord: FileRecord
- game/sound: common_types
- common/type_system: TypeSystem
- game/system: InputManager
- decompiler/IR2: FormElement
- game/kernel: kstrcpy()
- game/sound: SFXBlock
- test/decompiler: TEST()
- game/graphics: OceanTexture
- game/graphics: TextureAnimator.cpp
- decompiler/level_extractor: MercData.cpp
- goalc/compiler: Val
- goalc/build_level: ResLump.cpp
- game/graphics: DirectRenderer
- test/decompiler: TEST_F()
- game/overlord: jakx/iso_cd.cpp
- game/overlord: CDvdDriver
- game/sound: MidiHandler
- decompiler/data: FakePlayer
- game/graphics: LoaderInput
- lsp/state: Workspace
- decompiler: Config
- goalc/emitter: Register
- goalc/compiler: Util.cpp
- goalc/compiler: .get_none()
- game/graphics: CommonOceanRenderer
- common/util: SmallVector
- decompiler/IR2: FixedOperatorKind
- decompiler: Top-level CMakeLists.txt
- goalc/compiler: compilation/Type.cpp
- test: TEST()
- common/custom_data: MercModel
- decompiler/data: FullGrainInfo
- game/graphics: EyeRenderer
- decompiler/util: FieldId2
- common/util: gltf_util.cpp
- decompiler/util: FieldIdX
- game/overlord: ISO_VAGCommand
- scripts: os
- common/repl: Wrapper
- game/overlord: common/srpc.h
- game/overlord: ISO_VAGCommand
- decompiler/util: TP_Type
- test/offline: Taskfile.yml (root task 
- game/system: DisplayManager
- game/graphics: PrimBuildState
- decompiler/types2: SimpleExpression
- decompiler/util: FieldId
- game/graphics: Shadow2
- goalc/build_level: LevelFile
- goalc/emitter: InstructionX86
- game/overlord: jak3/streamlist.cpp
- goalc/build_level: LevelFile
- goalc/regalloc: VarAssignment
- common/formatter: FormatterTreeNode
- decompiler/data: game_text.cpp
- common/log: log.cpp
- game/sound: VoiceManager
- common/util: GameTextFontBank
- decompiler/IR2: AtomicOp.h
- decompiler/level_extractor: TFragment
- decompiler/level_extractor: array
- game/sound: BlockSoundHandler
- goalc/make: Tools.cpp
- goalc/build_level: LevelFile
- common/goos: Reader.cpp
- common/util: json
- goalc/emitter: ARM64_REG
- decompiler/analysis: cfg_builder.cpp
- goalc/build_level: jak3/collide.cpp
- goalc/build_level: tfrag3data
- game/graphics: Hfrag
- decompiler/extractor: parse_commented_json()
- decompiler/Disasm: InstructionAtom
- game/system: pair
- game/graphics: PcTextureAnimCodesJak3
- game/system: SystemThread
- goalc/emitter: InstructionARM64
- goalc/regalloc: AllocationInput
- decompiler/analysis: PrettyPrinter
- game/graphics: opengl.cpp
- decompiler/IR2: GenericOperator
- decompiler/types2: Instruction
- game/sound: SoundHandler
- tools: vendor.yaml (third-party
- game/graphics: GfxGlobalSettings
- game/settings: InputSettings
- common/cross_os_debug: xdbg.cpp
- common/custom_data: TFrag3Data.cpp
- game/graphics: OceanEnvmap
- game/sound: Player
- game/graphics: Loader
- goalc/build_level: jak2/collide.cpp
- goalc/emitter: RegisterInfo
- game/graphics: ShadowRenderer
- game/graphics: OpenGlDebugGui
- decompiler/IR2: FormStack.cpp
- decompiler/IR2: function
- game/graphics: Shrub
- common/global_profiler: GlobalProfiler
- common/util: path
- goalc/make: MakeSystem
- decompiler/IR2: Entry
- decompiler/level_extractor: MercCtrlHeader
- .github/workflows: AGENTS.md agent guide (O
- goalc/build_level: ResLump
- common/dma: GsRegisterAddress
- game/kernel: SpeedrunPracticeObjectiv
- game/sound: Voice
- game/graphics: OceanMid
- common/goos: InternedSymbolPtr
- game/graphics: Warp
- test: TEST()
- game/kernel: PickupType
- game/overlord: Jak2SoundCommand
- goalc/emitter: IGenX86.cpp
- common/type_system: Type
- decompiler/data: TexturePage
- game/graphics: Vu
- game/graphics: FramebufferTexturePair
- goalc/build_level: PatSurface
- goalc/build_level: color_quantization.cpp
- decompiler/util: DecompilerTypeSystem
- decompiler/IR2: Env
- decompiler/IR2: DerefToken
- game/graphics: Tree
- game/graphics: BlitDisplays
- game/graphics: Vu
- game/graphics: TextureAnimator.h
- game/sound: MIDISound
- game/tools: SubtitleEditor
- goalc/debugger: Debugger
- game/sound: ADSR
- decompiler/ObjectFile: ObjectFileDB_IR2.cpp
- common/math: Vector
- decompiler/util: sparticle_decompile.cpp
- decompiler/Disasm: OpcodeFields
- game/graphics: Merc2
- game/graphics: ClutBlender
- goalc/emitter: s64
- scripts/modding: update_mod_catalog.py
- goalc/emitter: TEST()
- game/sound: AmeHandler
- common/goos: PrettyPrinterNode
- game/sound: BinaryReader
- game/graphics: Vu
- game/graphics: FixedLayerDef
- game/overlord: jak3/iso_cd.cpp
- goalc/build_level: CollideFragMeshData
- decompiler/data: TextureDB
- decompiler/IR2: SetFormFormElement
- test/goalc: ArithmeticTests
- game/graphics: DepthCue
- game/mips2c: Cache
- game/overlord: VagCmd
- game/system: MouseDevice
- goalc/emitter: Register
- common/dma: GsTest
- decompiler/IR2: SimpleAtom
- game/graphics: ShaderId
- game/graphics: GlowRenderer
- goalc/compiler: .for_each_in_list()
- decompiler/Disasm: .parse_single_instructio
- game/kernel: jak2/kmachine_extras.cpp
- common/serialization: GameSubtitleBank
- decompiler/IR2: form_as_atom()
- goalc/debugger: FunctionDebugInfo
- goalc/emitter: emitter/Instruction.h
- game/sound: Grain
- decompiler/IR2: Kind
- game/graphics: OceanNear
- game/sound: LFOTracker
- common/custom_data: TfragTree
- decompiler/level_extractor: tfrag_tie_fixup.cpp
- .github/workflows: Build & Release OpenGOAL
- common/type_system: TypeFieldLookup.cpp
- decompiler/analysis: string
- decompiler/level_extractor: Ref
- game/mips2c: VfName
- goalc/data_compiler: DataObjectGenerator
- goalc/regalloc: RegAllocBasicBlock
- game/sce: sif_ee_memcard.cpp
- decompiler/ObjectFile: LinkedObjectFileCreation
- decompiler/types2: types2.cpp
- game/kernel: jak3/kmachine_extras.cpp
- game/kernel: jakx/kmachine_extras.cpp
- game/system: GameController
- goalc/build_level: CollideFragment
- goalc/build_level: EntityActor
- goalc/build_level: EntityActor
- common/goos: Node
- common/type_system: Field
- game/graphics: Draw
- goalc/build_level: CollideFragment
- goalc/compiler: SymbolInfo
- test: CodeTester
- lsp/protocol: CompletionItem
- goalc/build_actor: NodeWithTransform
- decompiler/level_extractor: BspHeader
- docs/progress-notes: Merc renderer (VU1 merc 
- goalc/build_actor: CompressedAnim
- goalc/compiler: Label
- goalc/emitter: VEX3
- test/goalc: TEST_F()
- decompiler/level_extractor: extract_level.cpp
- common/custom_data: MemoryUsageCategory
- common/dma: Kind
- common/goos: SourceText
- common/serialization: GameSubtitleDefinitionFi
- game/graphics: GraphicsData
- goalc/compiler: Kind
- decompiler/IR2: AtomicOpTypeAnalysis.cpp
- decompiler/IR2: ConditionElement
- game/graphics: PcTextureAnimCodesJak2
- game/overlord: VagStrListNode
- lsp/protocol: LSPSpec::from_json()
- test: TEST()
- common/formatter: FormFormattingConfig
- game/graphics: Merc2.cpp
- game/kernel: FocusStatus
- game/kernel: FocusStatus
- decompiler/Disasm: DecodeType
- decompiler/gui: decompiler_gui.py
- decompiler/IR2: SetVarElement
- game/mips2c: Cache
- game/overlord: CBaseFile
- game/overlord: ISO_DGOCommand
- game/overlord: ISO_DGOCommand
- game/sound: GrainType
- game/system: IOP
- goalc/build_level: Material
- goalc/debugger: DebugServer
- lsp/protocol: Diagnostic
- common/dma: GsPrim
- common/type_system: StateHandler
- decompiler/Disasm: Gpr
- game/mips2c: Gpr
- game/overlord: jakx/rpc_interface.h
- goalc/debugger: SourceStackFrame
- scripts/modding: package_texture_pack.py
- scripts/modding: create_mod_repo.py
- decompiler/IR2: AtomicOpForm.cpp
- decompiler/Disasm: Cop0
- decompiler/IR2: SimpleExpressionElement
- decompiler/IR2: Maps
- test/decompiler: TEST_F()
- game/kernel: common/kmemcard.cpp
- game/kernel: mc_slot_info
- game/kernel: FocusStatus
- game/mips2c: jak2_functions/merc_blen
- goalc/make: Tool
- goalc/emitter: .set_op2()
- tools/memory_dump_tool: memory_dump_tool/main.cp
- scripts/ci: lint-characters.py
- test/goalc: TEST_F()
- common/texture: process_tpage()
- common/util: Hunk
- decompiler/IR2: VariableNames
- decompiler/IR2: AsmOp
- decompiler/VuDisasm: VuDisassembler
- docs/img: Mod detail page (hero ba
- game/mips2c: FprName
- goalc/build_sbk: GrainData
- goalc/emitter: X86_REG
- common/custom_data: Vertex
- common/util: string_util.cpp
- decompiler/extractor: ExtractorErrorCode
- decompiler/analysis: variable_naming.cpp
- decompiler/level_extractor: extract_collide_frags()
- game/graphics: GLDisplay
- game/graphics: TexturePool.cpp
- goalc/compiler: algorithm
- common/type_system: StructureType
- common/util: read_iso_file.cpp
- decompiler/Function: ControlFlowGraph
- decompiler/VuDisasm: VuDisassembler.cpp
- game/mips2c: Cache
- game/mips2c: Cache
- game/overlord: jak3/rpc_interface.h
- game/overlord: SoundIOPInfo
- game/overlord: SoundIOPInfo
- goalc/build_level: collide_pack.cpp
- goalc/emitter: s64
- goalc/emitter: .set_disp()
- scripts/gsrc: utils.py
- goalc/build_actor: jak1/build_level.cpp
- decompiler/analysis: SSA
- decompiler/Disasm: Disasm/Register.cpp
- decompiler/Function: CfgVtx
- decompiler/IR2: LabelInfo
- decompiler/IR2: VectorFloatLoadStoreElem
- game/external: discord.cpp
- game/graphics: MercDebugStats
- game/kernel: VehicleType
- game/kernel: VehicleType
- game/mips2c: Cache
- game/overlord: SoundIopInfo
- goalc/compiler: SymbolInfoMap
- goalc/debugger: InstructionPointerInfo
- scripts/modding: switch_mod.py
- goalc/build_actor: animation_processing.cpp
- common/type_system: deftype.cpp
- common/serialization: subtitles_v2.cpp
- decompiler/analysis: analyze_ir2_register_usa
- decompiler/Function: FunctionName
- decompiler/level_extractor: PrototypeBucketTie
- decompiler/ObjectFile: LetRewriteStats
- decompiler/util: Kind
- game/mips2c: Cache
- game/system: IOP_Kernel.cpp
- goalc/compiler: IntegerMathKind
- test: TEST()
- common/util: font_utils_korean.cpp
- game/system: IopThread
- custom_assets/blender_plugins: gltf2_blender_extract.py
- decompiler/util: StackSpillMap
- decompiler/IR2: OpenGOALAsm
- game/overlord: Jak 2 Overlord Port Note
- game/graphics: LevelData
- game/graphics: OceanMid_PS2.cpp
- game/graphics: SpriteFrameData
- game/graphics: SpriteFrameDataJak1
- game/mips2c: Cache
- game/mips2c: Cache
- game/mips2c: Cache
- game/mips2c: Cache
- game/system: KeyboardDevice
- game/system: IOP_Kernel
- lsp/protocol: ProgressNotificationPayl
- decompiler/analysis: M2C_Block
- decompiler/analysis: SymbolMapBuilder
- decompiler/IR2: RegAccessSet
- decompiler/ObjectFile: LinkedWord
- game/kernel: codegen.h
- common/type_system: FieldReverseLookupOutput
- scripts/modding: sync_global_catalog.py
- decompiler/IR2: ArrayFieldAccess
- decompiler/ObjectFile: ObjectFileData
- game/graphics: Constants
- game/mips2c: Cache
- game/system: DisplayMode
- goalc/build_level: add_actors_from_json()
- goalc/listener: MemoryMapEntry
- scripts/ai: sys
- test/decompiler: TEST_F()
- decompiler/Function: Warnings.h
- docs/progress-notes: ETIE (environment-mapped
- lsp/protocol: TypeHierarchyItem
- game/graphics: ProgressRenderer
- game/mips2c: generic_tie.cpp
- game/mips2c: Cache
- game/mips2c: Cache
- game/mips2c: Cache
- game/overlord: Jak1SoundCommand
- game/overlord: SoundCommand
- goalc/build_level: collide_bvh.cpp
- goalc/emitter: Rt()
- lsp/protocol: CompletionItemKind
- common/util: os.cpp
- decompiler/ObjectFile: Stats
- game/graphics: SpriteHud2DPacket
- game/graphics: GpuTexture
- game/kernel: MasterConfig
- game/kernel: MouseInfo
- game/mips2c: MercBucketInfo
- game/mips2c: Cache
- game/overlord: SoundCommand
- goalc/build_actor: BuildActorParams
- goalc/compiler: CompilerSettings
- goalc/debugger: .describe_value_bits()
- goalc/debugger: DebugServer.cpp
- goalc/regalloc: RACache
- test/goalc: TEST_F()
- test: TEST()
- goalc/build_sbk: build_sbk.cpp
- common/dma: FixedChunkDmaCopier
- common/goos: ObjectType
- decompiler/data: StrFileReader.cpp
- docs/progress-notes: Control flow quirks of t
- game/graphics: TextureUploadHandler
- game/graphics: OceanTextureConstants
- game/sce: libpad.cpp
- game/system: DS5EffectsState_t
- game/system: EEInputEvent
- goalc/compiler: Atoms.cpp
- goalc/compiler: ConstantPropagation.cpp
- lsp/protocol: DocumentSymbol
- lsp/protocol: SymbolKind
- test: TEST()
- decompiler/analysis: get_defstate_entries()
- decompiler/IR2: AshElement
- goalc/retarget_anim: retarget_anim.cpp
- decompiler/VuDisasm: .decode()
- docs/modding: GitHub Actions Workflows
- game/graphics: BufferBlitState
- game/kernel: SpeedrunPracticeEntry
- game/kernel: SpeedrunPracticeEntry
- game/mips2c: jak1_functions/generic_m
- game/overlord: CDvdDriver
- goalc/build_level: Event
- goalc/regalloc: LiveInfo
- lsp/protocol: DidChangeTextDocumentPar
- common/util: T
- misc: test-script.py
- decompiler/analysis: final_output.cpp
- docs/modding: Taskfile.yml developer c
- docs/modding: How the Repository Works
- docs/setup: Visual Studio Setup Guid
- game/graphics: SpriteGlowOutput
- game/kernel: SpeedrunPracticeEntry
- game/overlord: jak3/dvd_driver.cpp
- game/sce: sceMcTblGetDir
- common/util: BinaryWriter
- common/util: TrieWithDuplicates
- decompiler/Disasm: FieldType
- decompiler/VuDisasm: AtomK
- game/graphics: OceanNear_PS2.cpp
- game/kernel: DiscordInfo
- game/mips2c: jak2_functions/generic_m
- game/mips2c: Cache
- game/mips2c: jak3_functions/generic_m
- game/mips2c: Cache
- game/mips2c: Cache
- game/overlord: Jak 3 Overlord TODO
- goalc/build_level: TieOutput
- goalc/compiler: Macro.cpp
- goalc/compiler: ConstantValue
- goalc/debugger: disassemble_x86_function
- test: test_emitter_arm64.cpp
- decompiler/level_extractor: ProgramInfo
- decompiler/util: FieldKind
- decompiler/VuDisasm: VuInstruction
- docs/scratch: TIE Format Document
- docs/progress-notes: Emerc (environment-mappe
- game/graphics: SpriteGlowData
- game/graphics: GoalTexture
- game/graphics: TexturePool
- game/kernel: McStatusCode
- game/kernel: MouseInfo
- game/mips2c: Cache
- game/mips2c: Cache
- game/mips2c: Cache
- goalc/build_sbk: SoundData
- .agents/skills: OpenGOAL Modding Knowled
- common/math: geometry.h
- common/util: CopyOnWrite
- decompiler/Disasm: Vi
- decompiler/ObjectFile: LinkedObjectFile
- docs/img: jak-project/iso_data/jak
- docs/progress-notes: GOAL language changelog 
- game/graphics: Uniforms
- game/kernel: Type
- game/kernel: Type
- game/kernel: Type
- game/kernel: SpeedrunPracticeObjectiv
- game/kernel: Type
- game/overlord: SoundIopInfo
- game/overlord: SoundPlayParams
- goalc/compiler: Lambda
- goalc/debugger: u32
- lsp/protocol: Hover
- common/serialization: GameTextDB
- decompiler/analysis: Mips2C_Output
- decompiler: DecompileHacks
- decompiler: string
- decompiler/level_extractor: JointAnimCompressedFixed
- docs/modding: How to Create a Mod
- docs/progress-notes: calc-animation-from-spr
- game/graphics: CollideMeshRenderer
- game/kernel: SpeedrunPracticeObjectiv
- game/overlord: common/sbank.cpp
- game/overlord: DmaQueueEntry
- game/overlord: jak3/dvd_driver.h
- game/overlord: CPageList
- game/overlord: DmaQueueEntry
- game/overlord: CPageList
- game/tools: imgui
- goalc/build_level: FileInfo
- goalc/retarget_anim: SkeletonJoints
- goalc/emitter: CodeTester.cpp
- common/audio: WaveFileHeader
- common/formatter: OpenGOAL Formatter docum
- common/sqlite: sqlite.h
- common/util: BinaryWriter.h
- common/util: Serializer.h
- decompiler/Function: CfgVtx.cpp
- docs/progress-notes: Annotated Jak 1 Sprite V
- docs/progress-notes: Six Sprite Glow Draws
- game/sound: Synth
- game/mips2c: Cache
- game/mips2c: Cache
- game/mips2c: ViName
- game/overlord: CPageManager
- game/overlord: CPageManager
- goalc/compiler: IR_FloatMath
- .agents/skills: Jak 2 merc geometry and 
- common: Deci2Header
- common/type_system: StructureDefResult
- decompiler/analysis: mips2c.cpp
- decompiler/analysis: run_variable_renaming()
- decompiler/data: GameCountResult
- decompiler/Disasm: Disasm/Register.h
- decompiler/Function: string
- decompiler/Function: Prologue
- decompiler/level_extractor: JointAnimCompressedFrame
- decompiler/VuDisasm: FieldK
- docs/img: Zed task spawner palette
- game/graphics: Merc2BucketRenderer
- game/graphics: SpriteGlowConsts
- game/graphics: GoalTexturePage
- game/kernel: MemoryCardOperation
- game/mips2c: Cache
- game/mips2c: Cache
- game/mips2c: Cache
- game/overlord: MsgType
- game/overlord: SoundInfo
- game/overlord: MsgType
- game/overlord: SoundInfo
- game/sound: fifo
- goalc/emitter: Immhi()
- test/goalc: TEST()
- lsp/protocol: FormattingOptions
- .agents/skills: GOAL language traps (sim
- common/audio: audio_formats.cpp
- decompiler/analysis: try_modify_input_types_f
- decompiler/Function: BasicBlock
- decompiler/Function: CfgVtx.h
- decompiler/level_extractor: common_formats.h
- decompiler: ObjectFileDB
- decompiler/VuDisasm: Kind
- docs/img: Visual Studio build conf
- docs/modding: mods-menu.gc registry (J
- docs/progress-notes: foreground-emerc (DMA ge
- docs/progress-notes: generic-merc-execute-all
- game/graphics: Shader
- game/kernel: BindAssignmentInfo
- game/mips2c: Cache
- game/mips2c: Cache
- game/mips2c: Cache
- game/mips2c: Cache
- game/mips2c: Cache
- game/overlord: CBaseFileSystem
- game/overlord: ISO_Hdr
- game/overlord: LogCategory
- game/overlord: jak3/pagemanager.cpp
- game/overlord: SoundPlayParams
- game/overlord: CBaseFileSystem
- game/overlord: ISO_Hdr
- game/overlord: jakx/pagemanager.cpp
- game/system: sdl_util.cpp
- game/tools: Entry
- goalc/emitter: InstructionSet
- .agents/skills: Register an in-game Mods
- .agents/skills: 3-layer mental model (ru
- test: TEST()
- game/graphics: Profiler.cpp
- common/util: image_resize.cpp
- common/util: unicode_util.cpp
- decompiler/analysis: FunctionAtomicOps
- decompiler/Function: Object
- decompiler/IR2: CondNoElseElement
- decompiler/IR2: StackSpillStoreElement
- decompiler/IR2: UseDefInfo
- decompiler/level_extractor: UncompressedJointAnim
- decompiler/level_extractor: extract_actors.cpp
- docs/progress-notes: Jak 1 kernel and engine 
- game/graphics: Vertex
- game/kernel: SpeedrunCustomCategory
- game/kernel: DiscordInfo
- game/mips2c: Cache
- game/mips2c: Cache
- game/mips2c: jakx_functions/generic_e
- game/mips2c: Cache
- goalc: compiler library
- game/overlord: BlockParams
- game/overlord: jak3/isocommon.h
- game/overlord: CBuffer
- game/overlord: CCache
- game/overlord: CPage
- game/overlord: s32
- game/overlord: SoundBankInfo
- game/overlord: BlockParams
- game/overlord: jakx/isocommon.h
- game/overlord: CBuffer
- game/overlord: CCache
- game/overlord: CPage
- game/overlord: s32
- game/overlord: SoundBankInfo
- goalc/build_sbk: create_sbk()
- .agents/skills: Documentation pre-flight
- common/custom_data: tie_normal_transform_v2(
- common/dma: AdGifData
- common/goos: string
- common/util: Trie
- decompiler/level_extractor: CompressedAnim
- decompiler/level_extractor: MercSwapInfo
- decompiler/types2: types2.h
- decompiler/util: TypeState
- docs/progress-notes: Warp Effect (framebuffer
- docs: game Runtime (C++ Engine
- game/graphics: VuLights
- game/mips2c: Rng
- game/mips2c: Cache
- game/mips2c: Cache
- game/overlord: Rpc_Player_Base_Cmd
- goalc/compiler: Kind
- lsp/protocol: ColorInformation
- game/sound: flava.h
- test: TEST()
- decompiler/Disasm: TEST()
- decompiler/Function: BlockVtx
- decompiler/IR2: ConditionalMoveFalseElem
- decompiler/IR2: CondWithElseElement
- decompiler/IR2: UntilElement
- decompiler/IR2: WhileElement
- decompiler/level_extractor: ArtData
- decompiler/util: DataParser.cpp
- docs/progress-notes: Generic TIE to ETIE conv
- docs/progress-notes: HFragment (Heightfield T
- game: runtime static library
- game/graphics: Profiler
- game/graphics: ScopedProfilerNode
- game/graphics: ProfilerNode
- game/graphics: TextureInput
- game/kernel: DiscordInfo
- game/kernel: SpeedrunCustomCategoryEn
- game/mips2c: Cache
- game/mips2c: Cache
- game/mips2c: Cache
- game/mips2c: Cache
- game/overlord: List
- game/overlord: RPC_Play_Cmd
- game/overlord: List
- game/overlord: RPC_Play_Cmd
- game/sce: stubs.cpp
- game/system: Semaphore
- goalc/compiler: BitFieldVal
- goalc/debugger: InstructionInfo
- lsp/handlers: initialize()
- lsp/state: WorkspaceAllTypesFile
- test/goalc: WithGameTests
- .agents/skills: Lightweight static objec
- custom_assets/blender_plugins: opengoal.py
- common/global_profiler: Event profiler (exact ti
- common/serialization: .write_subtitle_db_to_fi
- common/util: TieFullVertex
- decompiler/Disasm: AtomKind
- decompiler/IR2: CaseElement
- decompiler/IR2: GetMethodElement
- decompiler/IR2: ReturnElement
- decompiler/types2: Kind
- docs/progress-notes: Collide-Hash Fragment Bo
- docs: OpenGoal Documentation H
- game/graphics: TextureVRAMReference
- game/kernel: SpeedrunPracticeState
- game/kernel: SpeedrunPracticeState
- game/mips2c: jak1_functions/collide_e
- game/mips2c: Cache
- game/mips2c: Cache
- game/mips2c: Cache
- game/mips2c: Cache
- game/mips2c: Cache
- game/mips2c: Cache
- game/overlord: CMsg
- game/overlord: EIsoStatus
- game/overlord: Rpc_Player_Base_Cmd
- game/overlord: EIsoStatus
- game/sce: sceCdCLOCK
- game/sound: HandlePluginMessage()
- goalc/emitter: ObjectFileData
- .agents/skills: Ghost memory pitfall of 
- common/cross_os_debug: Kind
- decompiler/analysis: JumpTableBlock
- decompiler/data: data/dir_tpages.cpp
- decompiler/data: LinkedWordReader
- decompiler/level_extractor: ArtJointAnim
- decompiler/types2: Decompiler type pass v2
- docs/img: Launcher mod page screen
- docs/scratch: shrub-do-init-frame
- docs/progress-notes: Jak 1 TFRAG VU1 Micropro
- game/common: Language
- game/graphics: SpriteDataMem
- game/kernel: SpeedrunCustomCategoryEn
- game/kernel: SpeedrunCustomCategory
- game/kernel: SpeedrunCustomCategoryEn
- game/mips2c: jakx_functions/spatial_h
- game/overlord: FileCacheEntry
- game/overlord: jak3/iso.h
- game/overlord: ISO_LoadCommon
- game/overlord: RPC_Dgo_Cmd
- game/overlord: jakx/iso.h
- game/overlord: ISO_LoadCommon
- game/overlord: RPC_Dgo_Cmd
- game/overlord: CacheEntry
- goalc/build_level: Tie.cpp
- goal_src/user: User Profiles README
- goalc/emitter: Flags
- goalc/make: .get_additional_dependen
- goalc/regalloc: AssignmentRange
- goalc/regalloc: Op
- lsp/handlers: text_document/document_s
- lsp/state: OGGlobalIndex
- .agents/skills: 2-circuit architecture f
- common/goos: ShortInfo
- common: ListenerToTargetMsgKind
- decompiler/analysis: remap_color_move()
- docs/scratch: Sprite Distort VU1 Micro
- game/graphics: FramePlot
- game/graphics: SkyInput
- game/mips2c: jak1_functions/collide_f
- game/mips2c: jak1_functions/generic_e
- game/mips2c: Cache
- game/mips2c: Cache
- game/mips2c: jak2_functions/collide_f
- game/mips2c: jak2_functions/spatial_h
- game/mips2c: jak3_functions/collide_f
- game/mips2c: jak3_functions/spatial_h
- game/mips2c: jak3_functions/wvehicle_
- game/mips2c: jakx_functions/collide_f
- game/mips2c: Cache
- game/mips2c: jakx_functions/wvehicle_
- game/mips2c: Mips2C README
- game/overlord: Rpc_Player_Set_Ear_Trans
- game/overlord: RPC_Str_Cmd
- game/overlord: RPC_Str_Cmd
- goalc/emitter: Info
- lsp: lsp executable (OpenGOAL
- common/sqlite: GenericResponse
- common/type_system: parse_defenum()
- common/type_system: DeftypeResult
- decompiler/analysis: Register
- decompiler/Function: Break
- decompiler/Function: DelaySlotKind
- decompiler/level_extractor: CompressedFrame
- docs/img: .zed/debug.json debug co
- game/graphics: SpriteProgMem
- game/kernel: SQLResult
- game/kernel: jak3/kmalloc.cpp
- game/kernel: jakx/kmalloc.cpp
- game/mips2c: collide_probe.cpp
- game/mips2c: Cache
- game/overlord: VagCmdByte
- game/overlord: ISOFileDef
- game/overlord: RpcId
- game/overlord: ISOFileDef
- game/overlord: RpcId
- game/sound: bitfield
- game/system: State
- goalc/emitter: VF_ELEMENT
- goalc/compiler: Kind
- goalc/compiler: ArgumentInfo
- goalc/compiler: FieldInfo
- goalc/compiler: ValOrConstant
- lsp/handlers: text_document/type_hiera
- test/goalc: SharedCompiler
- .agents/skills: Lisp wiki common.md (all
- .agents/skills: Context pointers
- common: RegClass
- common/type_system: FieldLookupInfo
- common/versions: versions.cpp
- decompiler/analysis: convert_function_to_atom
- decompiler/Function: WhileLoop
- decompiler/level_extractor: JointAnimCompressedContr
- decompiler/VuDisasm: VuLowerOp6
- docs/progress-notes: asm-near (near DMA gener
- game/graphics: ProfilerStats
- game/graphics: ProfilerSort
- game/kernel: SQLResult
- game/kernel: from_json()
- game/kernel: from_json()
- game/kernel: from_json()
- game/mips2c: jak1_functions/collide_m
- game/mips2c: test_func.cpp
- game/mips2c: jak2_functions/collide_m
- game/mips2c: jak2_functions/lights.cp
- game/mips2c: jak3_functions/collide_m
- game/mips2c: Cache
- game/mips2c: jak3_functions/particle_
- game/mips2c: jakx_functions/lights.cp
- game/mips2c: jakx_functions/particle_
- game/overlord: jak3/iso_queue.h
- game/overlord: VagDir
- game/overlord: BufferType
- game/overlord: jakx/iso_queue.h
- game/overlord: VagDir
- game/overlord: BufferType
- goalc/compiler: DebugStats
- goalc/compiler: Settings
- goalc/data_compiler: compile_game_text()
- goalc/regalloc: initialize_unassigned()
- common/arm64: encoding.h
- common/formatter: Triangle of Death diagra
- common/type_system: BitfieldLookupInfo
- common/util: dialogs.h
- common/util: Filtered
- decompiler/analysis: insert_lets.h
- decompiler: RegisterTypeCast
- decompiler/Function: CondNoElse
- decompiler/Function: EntryVtx
- decompiler/Function: InfiniteLoopBlock
- game/graphics: DsFbo
- game/graphics: SpriteRecord
- game/overlord: State
- game/overlord: State
- goalc/build_sbk: TailGrowResult
- goalc/emitter: StaticData
- goalc/retarget_anim: RetargetOptions
- scripts/gsrc: iteratively-copy-decomp.
- scripts: Korean jamo glyph atlas
- .agents/skills: Porting gameplay and par
- .agents/skills: Process life cycle
- .agents/skills: Memory constants (EE_MAI
- decompiler/Function: ExitVtx
- game/common: GameLaunchOptions
- game/graphics: SmallProfilerStats
- game/kernel: u64
- game/overlord: FakeIsoEntry
- game/overlord: RamdiskFileRecord
- game/overlord: SoundRpcCommand
- game/overlord: DgoFno
- goalc/build_sbk: V2GrainEntries
- goalc/compiler: None
- goalc/debugger: StepKind
- goalc/emitter: PointerLink
- goalc/regalloc: Kind
- misc: blender-mcp
- .agents/skills: Jak 3 has no custom art-
- .agents/skills: PC settings and cheats p
- .agents/skills: Jak 3 powers and weapons
- .agents/skills: When to split a document
- docs/img: Robot guard model render
- docs/progress-notes: HFrag Montage Texture (1
- docs/scratch: draw-drawable-tree-insta
- goalc/data_compiler: PointerLinkRecord
- goalc/retarget_anim: matrix_from_node()
- misc: .prettierrc.json
- .agents/skills: Collision basics (root, 
- game/overlord: VagCmdPriListEntry
- .github: dependabot.yml
- .github/ISSUE_TEMPLATE: ISSUE_TEMPLATE config.ym
- .github/scripts: extract_build_unix.sh
- .github/scripts: extract_build_windows.sh
- goal_src/jak1: Jak 1 PC Port Sources RE
- scripts/shell: boot_game.sh
- scripts/shell: boot_kernel.sh
- scripts/shell: check.sh
- scripts/shell: decomp.sh
- scripts/shell: decomp2.sh
- scripts/shell: decomp3.sh
- scripts/shell: gc.sh
- scripts/shell: gk.sh
- scripts/shell: offline_test_git_branch.
- misc: test_code_coverage.sh
- misc: test_no_filter.sh
- misc: test.sh script
- .github: Offline allowlist (eight
- docs/progress-notes: Debug: Flames Applied Ev
- docs/progress-notes: hfrag finalize-dma (shad
- docs/progress-notes: init-work-from-current-h
- docs/progress-notes: time-of-day-interp-color

## God Nodes (most connected - your core abstractions)
1. `vector` - 1353 edges
2. `BucketId` - 771 edges
3. `Compiler` - 380 edges
4. `ObjectGenerator` - 377 edges
5. `TypeSpec` - 325 edges
6. `ExecutionContext` - 291 edges
7. `Val` - 281 edges
8. `InstructionKind` - 250 edges
9. `InstructionX86` - 238 edges
10. `Ptr` - 235 edges

## Surprising Connections (you probably didn't know these)
- `run_decompilation_process()` --calls--> `get_peak_rss()`  [INFERRED]
  decompiler/decompilation_process.cpp → common/util/os.cpp
- `main()` --calls--> `game_name_to_version()`  [INFERRED]
  goalc/build_level/main.cpp → common/versions/versions.cpp
- `Which agents read the knowledge base` --semantically_similar_to--> `task ai-link fills .claude/skills with links to shared skills`  [INFERRED] [semantically similar]
  .agents/skills/README.md → .claude/skills/README.md
- `Step 4: export glTF (.glb) from Blender` --references--> `tinygltf`  [INFERRED]
  custom_assets/README.md → CMakeLists.txt
- `MIPS instruction data for LSP` --conceptually_related_to--> `Mips2C converter`  [INFERRED]
  lsp/CMakeLists.txt → game/mips2c/readme.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Documentation standards enforced by documentalist** — agents_skills_documentalist_skill_english_only_rule, agents_skills_documentalist_skill_tone_and_conciseness, agents_skills_documentalist_skill_thematic_separation, agents_skills_documentalist_skill_no_decorative_icons, agents_skills_documentalist_skill_code_containment_rule, agents_skills_documentalist_skill_verification_rule [EXTRACTED 1.00]
- **Hot-reload ghost memory and the cold boot verification cluster** — agents_skills_engine_internals_repl_workflow_ghost_memory_pitfall, agents_skills_engine_internals_repl_workflow_cold_boot_verification_rule, agents_skills_goal_lisp_wiki_common_repl_ghost_memory, agents_skills_goal_lisp_wiki_common_symbols_linger_in_hot_repl, agents_skills_goal_lisp_wiki_common_clean_compile_not_validation [INFERRED 0.95]
- **Shared memory constants and per-game memory configuration** — agents_skills_goal_lisp_wiki_common_memory_constants, agents_skills_goal_lisp_wiki_jak1_memory, agents_skills_goal_lisp_wiki_jak2_memory, agents_skills_goal_lisp_wiki_jak3_memory [EXTRACTED 1.00]
- **Formatter pipeline phases** — common_formatter_readme_phase_build_tree, common_formatter_readme_phase_apply_config, common_formatter_readme_phase_apply_formatting, common_formatter_readme_phase_finalize [EXTRACTED 1.00]
- **Workflows restricted to the repository owner** — _github_workflows_build, _github_workflows_release, _github_workflows_sync_global_catalog, _github_workflows_sync_upstream [INFERRED 0.95]
- **Workflows guarded to the mother repository only** — _github_workflows_mod_suggestion_triage, _github_workflows_sync_global_catalog, _github_workflows_sync_upstream [INFERRED 0.95]
- **PS2 renderer reverse-engineering notes for the PC port** — docs_progress_notes_jak1_scratch_merc_merc_renderer, docs_progress_notes_jak1_scratch_shrub_asm_shrub_renderer, docs_progress_notes_jak1_scratch_generic_tie_to_etie_generic_tie, docs_progress_notes_bones_bones_gc, docs_progress_notes_blerc_blerc [INFERRED 0.85]
- **Mod release and launcher catalog pipeline** — docs_modding_guides_how_to_create_a_mod_release_steps, docs_modding_guides_github_workflows_release_yml, scripts_modding_update_mod_catalog, docs_modding_guides_mod_distribution_guide_index_json_catalog, docs_modding_guides_github_workflows_sync_global_catalog [INFERRED 0.95]
- **Decompiler object file processing stages** — decompiler_readme_objectfiledb, decompiler_readme_process_link_data, decompiler_readme_find_code, decompiler_readme_process_labels, decompiler_readme_basic_block_finding, decompiler_readme_prologue_epilogue_analysis [INFERRED 0.85]
- **Emerc Per-Frame Draw Pipeline** — docs_progress_notes_jak2_emerc_foreground_engine_execute, docs_progress_notes_jak2_emerc_foreground_draw, docs_progress_notes_jak2_emerc_foreground_emerc, docs_progress_notes_jak2_emerc_foreground_execute_cpu_vu0_engines, docs_progress_notes_jak2_emerc_emerc_vu1_init_buffers [EXTRACTED 1.00]
- **Joint Animation Decompression Pipeline** — docs_progress_notes_joint_decompressor_flatten_joint_control_to_spr, docs_progress_notes_joint_decompressor_make_joint_jump_tables, docs_progress_notes_joint_decompressor_calc_animation_from_spr, docs_progress_notes_joint_decompressor_decompress_fixed_data_to_accumulator, docs_progress_notes_joint_decompressor_decompress_frame_data_to_accumulator, docs_progress_notes_joint_decompressor_clear_frame_accumulator [INFERRED 0.85]
- **HFrag Drawing Process** — docs_progress_notes_jak3_hfrag_init_work_from_current_hfrag, docs_progress_notes_jak3_hfrag_pick_level_of_detail, docs_progress_notes_jak3_hfrag_trim_draw_lists, docs_progress_notes_jak3_hfrag_time_of_day_interp_colors_scratch, docs_progress_notes_jak3_hfrag_generate_dma, docs_progress_notes_jak3_hfrag_method_23_texture_dma, docs_progress_notes_jak3_hfrag_finalize_dma [EXTRACTED 1.00]
- **Mips2C conversion, linking and invocation pipeline** — game_mips2c_readme_mips2c_converter, game_mips2c_readme_hacks_jsonc_registration, game_mips2c_readme_link_callbacks, game_mips2c_mips2c_table_cpp_game_mips2c_mips2c_table, game_mips2c_readme_get_mips2c_accessor, game_mips2c_readme_execution_context [EXTRACTED 1.00]
- **Distort sprite generation on VU1** — docs_scratch_sprite_distort_vu1_sprite_flag_resolution, docs_scratch_sprite_distort_vu1_sine_tables, docs_scratch_sprite_distort_vu1_pie_slice_circle, docs_scratch_sprite_distort_vu1_double_buffered_gs_output [EXTRACTED 1.00]
- **Developer environment setup guides (OS and IDE)** — docs_setup_system_windows, docs_setup_system_linux, docs_setup_system_macos, docs_setup_system_docker, docs_setup_dev_vs, docs_setup_dev_vscode, docs_setup_dev_zed [INFERRED 0.85]
- **Per-OS Taskfile variable files included by the root Taskfile** — scripts_tasks_taskfile_windows, scripts_tasks_taskfile_linux, scripts_tasks_taskfile_darwin [EXTRACTED 1.00]
- **Modding repository lifecycle tasks (create, switch, sync, catalog, texture packs)** — taskfile_modding_new_mod, taskfile_modding_switch, taskfile_modding_sync_branch, taskfile_modding_sync_all, taskfile_modding_sync_catalog, taskfile_modding_package_texture_pack [INFERRED 0.85]
- **Vendored libraries patched by PR #1632 for UTF-8 paths on Windows** — vendor_third_party_fpng, vendor_third_party_stb_image, vendor_third_party_tiny_gltf [EXTRACTED 1.00]
- **Launcher add-a-mod tutorial (steps 1 to 4)** — docs_img_add_mod_1, docs_img_add_mod_2, docs_img_add_mod_3, docs_img_add_mod_4 [INFERRED 0.85]
- **Mod install pipeline: download, extract, decompile, compile, done** — docs_img_add_mod_4_step_download_mod, docs_img_add_mod_4_step_extract_verify, docs_img_add_mod_4_step_decompile, docs_img_add_mod_4_step_compile, docs_img_add_mod_4_step_done [EXTRACTED 1.00]
- **Ways to obtain a mod in the launcher: source URL, catalog, external site** — docs_img_add_mod_1_mod_source_url_field, docs_img_add_mod_2_mods_catalog_page, docs_img_add_mod_2_external_mods_section [INFERRED 0.75]
- **Add-a-mod flow: launcher Play button to in-game Mods entry** — docs_img_add_mod_5_peaceful_haven_city_mod, docs_img_add_mod_5_play_button, docs_img_add_mod_6_mods_menu, docs_img_add_mod_6_crimson_blueguard_peaceful_entry [INFERRED 0.85]
- **Zed C++ build workflow: Generate CMake then Build Project (Debug or Release)** — docs_img_editors_zed_generate_cmake_debug_task, docs_img_editors_zed_generate_cmake_release_task, docs_img_editors_zed_build_project_debug_task, docs_img_editors_zed_build_project_release_task [INFERRED 0.85]
- **goalc REPL session in Zed: banner, nREPL, (lt), (mi)** — docs_img_editors_zed_goalc_repl_banner, docs_img_editors_zed_nrepl_port_8181, docs_img_editors_zed_repl_lt_command, docs_img_editors_zed_repl_mi_command [EXTRACTED 1.00]
- **Zed debug.json task set (REPL, Game, Tests)** — docs_img_editors_zed_zed_run_example_repl_jak_1_2_3_tasks, docs_img_editors_zed_zed_run_example_game_jak_1_2_3_tasks, docs_img_editors_zed_zed_run_example_tests_unit_draft_only_task [EXTRACTED 1.00]
- **Jak 1 disc contents expected in iso_data/jak1** — docs_img_iso_data_help_game_data_folders, docs_img_iso_data_help_scus_971_24, docs_img_iso_data_help_disc_root_files [EXTRACTED 1.00]
- **Windows Visual Studio build walkthrough (open CMake, pick Release clang, Build All)** — docs_img_windows_open_project, docs_img_windows_release_build, docs_img_windows_build_all [INFERRED 0.85]

## Communities (972 total, 83 thin omitted)

### Community 0 - "Renderer Bucket IDs"
Cohesion: 0.00
Nodes (771): BucketId, ALPHA_TEX_LEVEL0, ALPHA_TEX_LEVEL1, BILLBOARD_L0_SHRUB, BILLBOARD_L1_SHRUB, BILLBOARD_L2_SHRUB, BILLBOARD_L3_SHRUB, BILLBOARD_L4_SHRUB (+763 more)

### Community 1 - "GOAL Compiler Core"
Cohesion: 0.01
Nodes (23): Compiler, m_allow_inconsistent_definition_symbols, m_debug_stats, m_debugger, m_global_constants, m_global_env, m_goos, m_inlineable_functions (+15 more)

### Community 2 - "Game Kernel Runtime"
Cohesion: 0.02
Nodes (53): FixedChunkDmaCopier::FixedChunkDmaCopier(), compress_zstd(), compress_zstd_no_header(), decompress_zstd(), Timer, _startTime, timespec, Exit() (+45 more)

### Community 3 - "Overlord ISO and IOP"
Cohesion: 0.02
Nodes (84): StrFileHeaderJ1(), get_as(), GoalStackArgs, args, RpcCall_wrapper(), SoundBank, VagDirEntry, SoundRpcCommand (+76 more)

### Community 4 - "x86 Emitter and Codegen"
Cohesion: 0.03
Nodes (219): add_f32_f32(), add_gpr64_gpr64(), add_gpr64_imm(), add_gpr64_imm32s(), add_gpr64_imm8s(), add_vf(), and_gpr64_gpr64(), blend_vf() (+211 more)

### Community 5 - "mips2c Execution Context"
Cohesion: 0.02
Nodes (40): count_leading_zeros_u32(), BC, w, x, y, z, DEST, NONE (+32 more)

### Community 6 - "Tfrag3 and TIE Data"
Cohesion: 0.01
Nodes (179): Blerc, float_data, int_data, kTargetIdxTerminator, BlercFloatData, v, get_second_draw_category(), Hfragment (+171 more)

### Community 7 - "Compiler IR and Regalloc"
Cohesion: 0.01
Nodes (126): IR, IR_Asm, m_use_coloring, IR_AsmAdd, m_dst, m_src, IR_AsmBreak, IR_AsmFNop (+118 more)

### Community 8 - "Decompiler Utilities"
Cohesion: 0.02
Nodes (35): SignalInfo, kind, msg, TypeSystem, ArgumentGuard, DecompilerTypeSystem, Form, FormPool (+27 more)

### Community 9 - "Listener and Sockets"
Cohesion: 0.02
Nodes (80): accept_socket(), address_to_string(), close_socket(), connect_socket(), open_socket(), read_from_socket(), select_and_accept_socket(), set_socket_option() (+72 more)

### Community 10 - "DMA Follower and Sprite3"
Cohesion: 0.02
Nodes (108): DmaFollower, m_base, m_ended, m_sp, m_stack, m_tag_offset, DmaTransfer, data (+100 more)

### Community 11 - "MIPS Instruction Set"
Cohesion: 0.01
Nodes (183): InstructionKind, ABSS, ADDAS, ADDS, ADDU, AND, BC1F, BC1FL (+175 more)

### Community 12 - "Compiler Test Runner"
Cohesion: 0.02
Nodes (70): exec_runtime(), CompilerTestRunner, c, tests, createDirIfAbsent(), Environment, escaped_string(), getFailedDir() (+62 more)

### Community 13 - "Compiler Environments"
Cohesion: 0.02
Nodes (90): CodeGenerator::CodeGenerator(), alloc_env(), alloc_val(), BlockEnv, BlockEnv::BlockEnv(), end_label, name, return_types (+82 more)

### Community 14 - "Decompiler Form Matching"
Cohesion: 0.06
Nodes (101): write_from_top_level_form(), is_nonvirtual_state_with_inherit(), is_virtual_state_with_nonvirtual_inherit(), rewrite_virtual_defstate(), get_defskelgroup_entries(), get_defskelgroup_entries_jak3(), fix_up_abs(), fix_up_abs_2() (+93 more)

### Community 15 - "Decompiler Atomic Ops"
Cohesion: 0.02
Nodes (54): AsmOp::AsmOp(), CallOp, m_arg_vars, m_call_type, m_call_type_set, m_function_var, m_return_var, ConditionalMoveFalseOp (+46 more)

### Community 16 - "Overlord Jak X Streams"
Cohesion: 0.03
Nodes (137): complete_dma_now(), dma_intr_hack(), DMA_SendToEE(), DMA_SendToSPUAndSync(), DmaInterruptHandlerHack, cb, chan, countdown (+129 more)

### Community 17 - "GS Registers and Depth Cue"
Cohesion: 0.02
Nodes (105): BlendMode, DEST, INVALID, SOURCE, ZERO_OR_FIXED, GsAlpha, data, GsFrame (+97 more)

### Community 18 - "LSP Handlers"
Cohesion: 0.02
Nodes (80): intersection(), Function, Matrix, data, ObjectiveZoneInitParams, v1, v2, Vector (+72 more)

### Community 19 - "Compiler Values and Regs"
Cohesion: 0.02
Nodes (83): coerce_to_reg_type(), IR_AsmAdd::IR_AsmAdd(), IR_AsmPop::IR_AsmPop(), IR_AsmPush::IR_AsmPush(), IR_AsmSub::IR_AsmSub(), IR_BlendVF::IR_BlendVF(), IR_FloatToInt::IR_FloatToInt(), IR_FunctionAddr::IR_FunctionAddr() (+75 more)

### Community 20 - "Decompiler IR2 Env"
Cohesion: 0.02
Nodes (84): ContainerType, ARRAY, INLINE_ARRAY, NONE, StackStructureHint, container_size, container_type, element_type (+76 more)

### Community 21 - "Generic2 Renderer"
Cohesion: 0.02
Nodes (105): Adgif, data, fix, frag, mode, next, tbp, uses_hud (+97 more)

### Community 22 - "Overlord Jak 2 Buffers"
Cohesion: 0.02
Nodes (143): LookMbx(), WaitMbx(), Buffer, data_buffer_idx, decomp_buffer, decompressed_size, free_pages, next (+135 more)

### Community 23 - "Sound Player RPC"
Cohesion: 0.03
Nodes (122): AllocateSound(), CalculateAngle(), CalculateFalloffVolume(), CleanSounds(), GetPan(), GetVolume(), KillSoundsInGroup(), LookupSound() (+114 more)

### Community 24 - "Form Expression Analysis"
Cohesion: 0.07
Nodes (137): condition_uses_float(), get_condition_num_args(), AbsElement::update_from_stack(), allocate_fixed_op(), ArrayFieldAccess::update_from_stack(), ArrayFieldAccess::update_with_val(), AshElement::update_from_stack(), AsmBranchElement::push_to_stack() (+129 more)

### Community 25 - "Overlord Jak 1 ISO Queue"
Cohesion: 0.02
Nodes (127): DMA_Sync(), bswap(), CalculateVAGVolumes(), CancelDGO(), CheckVAGStreamProgress(), CopyDataToEE(), CopyDataToIOP(), GetPlayPos() (+119 more)

### Community 26 - "Overlord Jak 3 Streams"
Cohesion: 0.03
Nodes (116): DoSetVol(), complete_dma_now(), dma_intr_hack(), DMA_SendToEE(), DMA_SendToSPUAndSync(), DmaInterruptHandlerHack, cb, chan (+108 more)

### Community 27 - "Decompiler Form Elements"
Cohesion: 0.02
Nodes (57): AbsElement::AbsElement(), AsmBranchElement::AsmBranchElement(), AtomicOpElement, AtomicOpElement::AtomicOpElement(), m_op, BreakElement::BreakElement(), CaseElement::CaseElement(), CastElement::CastElement() (+49 more)

### Community 28 - "Kernel Memory and DGO Link"
Cohesion: 0.03
Nodes (78): arm64_read_mov32(), arm64_write_mov32(), kstrcpyup(), RpcBind(), RpcBusy(), RpcCall(), RpcSync(), arm64_other_seg_mov32_link_v3() (+70 more)

### Community 29 - "Kernel Print and Call GOAL"
Cohesion: 0.03
Nodes (100): basename_goal(), FileExists(), fileio_init_globals(), FileLength(), FileLoad(), FileSave(), kstrcat(), kstrinsert() (+92 more)

### Community 30 - "Level Extractor Shrub"
Cohesion: 0.02
Nodes (108): CollideFragment, bsphere, mesh, DrawableInlineArrayCollideFragment, bsphere, collide_fragments, id, length (+100 more)

### Community 31 - "Compiler Static Data"
Cohesion: 0.03
Nodes (58): float_as_u32(), integer_fits(), Compiler::compile_bitfield_definition(), Compiler::compile_new_static_structure(), Compiler::compile_new_static_structure_or_basic(), Compiler::compile_static(), Compiler::compile_static_no_eval_for_pairs(), Compiler::compile_static_pair() (+50 more)

### Community 32 - "Texture Animator"
Cohesion: 0.02
Nodes (130): Bool, b, TextureAnimator, kFinalSkyHiresTextureSize, kFinalSkyTextureSize, kFinalSlimeTextureSize, kNumSkyHiresNoiseLayers, kNumSkyNoiseLayers (+122 more)

### Community 33 - "Overlord Jak 2 Streams"
Cohesion: 0.03
Nodes (97): DMA_SendToSPUAndSync(), intr(), ProcessVAGData(), DoQueue(), DoSetVol(), DoStop(), DoStopAll(), HandlePluginRequests() (+89 more)

### Community 34 - "Offline Test Orchestration"
Cohesion: 0.02
Nodes (88): game_name_to_version(), main(), PatResult, ignore, pat, set, main(), OfflineTestConfig (+80 more)

### Community 35 - "Tie3 and Tfrag Renderer"
Cohesion: 0.03
Nodes (82): cull_check_all_slow(), DoubleDraw, aref_first, aref_second, color_mult, kind, DoubleDrawKind, AFAIL_NO_DEPTH_WRITE (+74 more)

### Community 36 - "Data Decompile and TypeSpec"
Cohesion: 0.04
Nodes (70): TypeSpec, m_arguments, m_tags, m_type, TypeTag, name, value, AshElement::AshElement() (+62 more)

### Community 37 - "mips2c TIE Methods"
Cohesion: 0.02
Nodes (60): Cache, fake_scratchpad_data, execute(), vcallms48(), execute(), execute(), execute(), Cache (+52 more)

### Community 39 - "GOOS Interpreter"
Cohesion: 0.08
Nodes (36): build_list_with_spliced_tail(), Interpreter, builtin_forms, disable_printing, gensym_id, global_environment, goal_env, m_custom_forms (+28 more)

### Community 40 - "game/graphics: BucketRenderer"
Cohesion: 0.02
Nodes (67): BucketRenderer, m_enabled, m_my_id, m_name, EmptyBucketRenderer, EmptyBucketRenderer::EmptyBucketRenderer(), EyeRenderer, Fbo (+59 more)

### Community 41 - "goalc/compiler: IR.cpp"
Cohesion: 0.05
Nodes (27): empty_pair_offset_from_s7(), false_symbol_offset(), arm64_load_symbol_value(), get_no_color_reg(), get_reg(), get_reg_asm(), get_stack_offset(), IR_FunctionCall::IR_FunctionCall() (+19 more)

### Community 42 - "game/sce: iop.cpp"
Cohesion: 0.02
Nodes (93): call_start(), start_overlord(), InitRamdisk(), VBlank_Handler(), AddToCircularList(), BreakCircularList(), InitList(), MakeCircularList() (+85 more)

### Community 43 - "decompiler/analysis: AtomicOp"
Cohesion: 0.09
Nodes (99): add_clobber_if_unwritten(), convert_1(), convert_12(), convert_1_allow_asm(), convert_2(), convert_3(), convert_4(), convert_5() (+91 more)

### Community 44 - "decompiler/level_extractor: string"
Cohesion: 0.02
Nodes (88): Drawable, DrawableActor, actor, bsphere, DrawableAmbient, ambient, bsphere, DrawableInlineArrayTFrag (+80 more)

### Community 45 - "game/graphics: TFragment"
Cohesion: 0.02
Nodes (91): TFragmentTreeKind, DIRT, ICE, INVALID, LOWRES, LOWRES_TRANS, NORMAL, TRANS (+83 more)

### Community 46 - "game/graphics: OpenGLRenderer"
Cohesion: 0.02
Nodes (68): offset_of_s7, BucketCategory, GENERIC, MAX_CATEGORIES, MERC, OCEAN, OTHER, SHRUB (+60 more)

### Community 47 - "common/goos: Object"
Cohesion: 0.03
Nodes (38): ArgumentSpec, named, rest, unnamed, varargs, ArrayObject, data, build_list() (+30 more)

### Community 48 - "decompiler/level_extractor: extract_merc.cpp"
Cohesion: 0.03
Nodes (96): add_custom_model_to_level(), blerc_pack(), blerc_vertex_convert(), BlercVtxFloat, base, dest, targets, BlercVtxFloatTarget (+88 more)

### Community 49 - "goalc/build_actor: jak1/build_actor.cpp"
Cohesion: 0.03
Nodes (74): ArtElement, pad, ArtGroup, elts, info, joint_map, mdl, ArtJointAnim (+66 more)

### Community 50 - "game/kernel: common/kmachine.cpp"
Cohesion: 0.04
Nodes (91): get_font_bank_from_game_version(), RendererTreeType, INVALID, NONE, TFRAG3, TIE3, register_screen_shot_settings(), bool_to_symbol() (+83 more)

### Community 51 - "goalc/build_actor: jak3/build_actor.cpp"
Cohesion: 0.03
Nodes (72): Art, length, lump, name, ArtElement3, master_art_group_index, master_art_group_name, pad (+64 more)

### Community 52 - "decompiler/level_extractor: extract_tie.cpp"
Cohesion: 0.04
Nodes (91): DrawableInlineArray, add_vertices_and_static_draw(), AdgifInfo, alpha_val, clamp_val, combo_tex, first_w, num_mips (+83 more)

### Community 53 - "common/type_system: type_system/Type.cpp"
Cohesion: 0.04
Nodes (21): BasicType, m_final, BitField, m_name, m_offset, m_size, m_skip_in_static_decomp, m_type (+13 more)

### Community 54 - "decompiler/IR2: bitfields.cpp"
Cohesion: 0.04
Nodes (55): BitFieldType, m_fields, BitfieldAccessElement, BitfieldAccessElement::BitfieldAccessElement(), m_base, m_current_result, m_got_pcpyud, m_steps (+47 more)

### Community 55 - "decompiler/IR2: Kind"
Cohesion: 0.02
Nodes (109): Kind, ABS_S, ADD, ADD_S, ALWAYS, AND, BREAK, CRASH (+101 more)

### Community 56 - "decompiler/Disasm: TEST()"
Cohesion: 0.02
Nodes (40): ADDIU, ANDI, CVTSW, CVTWS, DADDIU, DADDU, DSLL, DSLL32 (+32 more)

### Community 57 - "goalc/emitter: ObjectGenerator.cpp"
Cohesion: 0.03
Nodes (57): FunctionData, debug, instruction_to_byte_in_data, instructions, ir_to_instruction, min_align, FunctionDebugInfo, FunctionRecord (+49 more)

### Community 59 - "goalc/build_actor: jak2/build_actor.cpp"
Cohesion: 0.03
Nodes (66): ArtGroup, elts, info, joint_map, mdl, ArtJointAnim, artist_base, artist_step (+58 more)

### Community 60 - "game/kernel: jak2/kscheme.cpp"
Cohesion: 0.07
Nodes (88): flush_icache_goal(), Symbol4, foo, InitListener(), sql_query_sync(), data, initialize_sql_db(), InitMachine_PCPort() (+80 more)

### Community 61 - "goalc/compiler: throw_compiler_error()"
Cohesion: 0.07
Nodes (72): Compiler::compile_asm_abs_vf(), Compiler::compile_asm_add(), Compiler::compile_asm_blend_vf(), Compiler::compile_asm_div_vf(), Compiler::compile_asm_int128_math2_imm_u8(), Compiler::compile_asm_int128_math3(), Compiler::compile_asm_inv_sqrt_vf(), Compiler::compile_asm_jr() (+64 more)

### Community 62 - "decompiler/level_extractor: GameVersion"
Cohesion: 0.08
Nodes (34): max_symbols(), GameVersion, Jak1, Jak2, Jak3, JakX, copy_dma_to_vector(), get_child_stride() (+26 more)

### Community 63 - "game/kernel: cprintf()"
Cohesion: 0.07
Nodes (86): build_revision(), init_common_pc_port_functions(), cprintf(), crc32(), DecodeFileName(), MakeFileName(), KernelCheckAndDispatch(), link_and_exec() (+78 more)

### Community 64 - "game/kernel: jak3/kscheme.cpp"
Cohesion: 0.07
Nodes (88): InitListener(), sql_query_sync(), initialize_sql_db(), InitMachine_PCPort(), InitMachineScheme(), kopen(), alloc_and_init_type(), alloc_from_heap() (+80 more)

### Community 65 - "game/overlord: GetThreadId()"
Cohesion: 0.05
Nodes (68): DMA_SendToEE(), PrintActiveSounds(), LoadMusic(), LoadSoundBank(), DGOThread(), Thread_Server(), RPC_Loader(), Thread_Loader() (+60 more)

### Community 66 - "game/graphics: DirectRenderer2"
Cohesion: 0.03
Nodes (57): Debug, disable_mip, DirectRenderer2, DirectRenderer2::DirectRenderer2(), DirectRenderer2::Draw::to_single_line_string(), DirectRenderer2::Draw::to_string(), m_current_state_has_open_draw, m_debug (+49 more)

### Community 67 - "game/graphics: AdgifHelper"
Cohesion: 0.03
Nodes (44): AdgifHelper, m_alpha, m_data, m_tex0, m_tex1, blend_sky_fast(), blend_sky_initial_fast(), SkyBlendCPU (+36 more)

### Community 68 - "decompiler/Function: Function"
Cohesion: 0.04
Nodes (62): true_symbol_offset(), get_gpr_store_offset_as_int(), is_always_branch(), is_branch(), is_gpr_2_imm_int(), is_gpr_3(), is_gpr_load(), is_gpr_store() (+54 more)

### Community 69 - "decompiler/analysis: analyze_inspect_method.c"
Cohesion: 0.06
Nodes (75): allow_guess(), detect(), FieldPrint, array_size, DYNAMIC_ARRAY, field_name, field_type_name, format (+67 more)

### Community 70 - "game/kernel: jakx/kscheme.cpp"
Cohesion: 0.08
Nodes (86): MsgWarn(), InitListener(), InitMachine_PCPort(), InitMachineScheme(), kopen(), alloc_and_init_type(), alloc_from_heap(), alloc_heap_memory() (+78 more)

### Community 71 - "decompiler/IR2: StaticInfo"
Cohesion: 0.02
Nodes (71): read_static_group_data(), read_static_part_data(), run_defpartgroup(), ClothParams, alt_tex_name, alt_tex_name2, alt_tex_name3, anchor_points (+63 more)

### Community 72 - "goalc/build_level: Region"
Cohesion: 0.03
Nodes (50): add_regions_from_json(), DrawableInlineArrayRegionPrim, data, DrawableRegionFace, bsphere_override, data, face_data_slot, DrawableRegionPrim (+42 more)

### Community 73 - "goalc/build_level: Region"
Cohesion: 0.03
Nodes (50): add_regions_from_json(), DrawableInlineArrayRegionPrim, data, DrawableRegionFace, bsphere_override, data, face_data_slot, DrawableRegionPrim (+42 more)

### Community 74 - "game/system: mutex"
Cohesion: 0.03
Nodes (43): mutex, SplashScreen, data, height, ready, width, BackgroundJob, payload (+35 more)

### Community 75 - "decompiler/ObjectFile: ObjectFileDB"
Cohesion: 0.05
Nodes (36): run_decompilation_process(), main(), are_objects_the_same(), for_each_function(), for_each_function_def_order(), for_each_function_def_order_in_obj(), for_each_function_in_seg(), for_each_obj() (+28 more)

### Community 76 - "decompiler/level_extractor: extract_tfrag.cpp"
Cohesion: 0.04
Nodes (73): VifCode, immediate, interrupt, kind, num, VifCodeStcycl, cl, wl (+65 more)

### Community 77 - "goalc/compiler: TypeDocumentation"
Cohesion: 0.03
Nodes (87): Compiler::generate_per_file_symbol_info(), ArgumentDocumentation, description, is_mutated, is_optional, is_unused, name, type (+79 more)

### Community 79 - "test/decompiler: FormRegressionTest.cpp"
Cohesion: 0.03
Nodes (25): FormRegressionTest, dts, parser, FormRegressionTest::TestData::add_string_at_label(), FormRegressionTestJak1, FormRegressionTestJak2, parse_var_json(), RegisterTypeCast (+17 more)

### Community 80 - "decompiler/VuDisasm: VuInstrK"
Cohesion: 0.02
Nodes (92): VuInstrK, ADD, ADDA, ADDAbc, ADDbc, ADDi, ADDq, B (+84 more)

### Community 81 - "game/common: Vf"
Cohesion: 0.04
Nodes (26): Accumulator, data, copy_vector(), Mask, NONE, w, x, xw (+18 more)

### Community 82 - "test/goalc: test_vector_float.cpp"
Cohesion: 0.04
Nodes (51): TEST_P(), VectorFloatParameterizedTestFixtureWithRunner_OneOperandQuotient, templateFile, VectorFloatParameterizedTestFixtureWithRunner_SingleOperand, templateFile, VectorFloatParameterizedTestFixtureWithRunner_TwoOperand, templateFile, VectorFloatParameterizedTestFixtureWithRunner_TwoOperandACC (+43 more)

### Community 83 - "game/system: InputBindingGroups"
Cohesion: 0.04
Nodes (59): pc_reset_bindings_to_defaults(), pc_set_waiting_for_bind(), AnalogIndex, LEFT_X, LEFT_Y, RIGHT_X, RIGHT_Y, CommandBinding (+51 more)

### Community 84 - "common/dma: DrawMode"
Cohesion: 0.07
Nodes (29): AlphaBlend, DISABLED, SRC_0_DST_DST, SRC_0_FIX_DST, SRC_0_SRC_DST, SRC_DST_FIX_DST, SRC_DST_SRC_DST, SRC_SRC_SRC_SRC (+21 more)

### Community 85 - "game/mips2c: get_fake_spad_addr2()"
Cohesion: 0.03
Nodes (68): execute(), Cache, fake_scratchpad_data, exec_mpg(), execute(), Cache, fake_scratchpad_data, generic_envmap_proc (+60 more)

### Community 86 - "decompiler/level_extractor: Level"
Cohesion: 0.06
Nodes (65): Level, collision, hfrag, index_textures, level_name, merc_data, shrub_trees, textures (+57 more)

### Community 87 - "game/overlord: FileRecord"
Cohesion: 0.04
Nodes (62): fake_iso_FS_Init(), FS_Find(), FS_FindIN(), FS_GetLength(), get_file_path(), LoadMusicTweaks(), MakeISOName(), ExitIOP() (+54 more)

### Community 88 - "game/sound: common_types"
Cohesion: 0.04
Nodes (26): read(), PerGameVersion, data, Billboard, DecompilerTypeSystem, LinkedObjectFile, sceDmaChan, sceDmaSync() (+18 more)

### Community 89 - "common/type_system: TypeSystem"
Cohesion: 0.09
Nodes (12): allow_inline(), find_best_field_in_structure(), throw_typesystem_error(), TypeSystem, m_allow_redefinition, m_forward_declared_method_counts, m_forward_declared_types, m_old_types (+4 more)

### Community 90 - "game/system: InputManager"
Cohesion: 0.04
Nodes (23): pc_clear_trigger_effect(), TriggerEffectOption, BOTH, LEFT, RIGHT, InputManager, ee_event_queue, m_auto_hide_mouse (+15 more)

### Community 91 - "decompiler/IR2: FormElement"
Cohesion: 0.03
Nodes (25): alloc_single_element_form(), CastElement, m_numeric, m_source, m_type, CfgVtx, CounterLoopElement, m_body (+17 more)

### Community 92 - "game/kernel: kstrcpy()"
Cohesion: 0.05
Nodes (68): exit, kstrcpy(), InitRPC(), StopIOP(), GoalProtoHandler(), GoalProtoStatus(), InitGoalProto(), kdsnetm_init_globals_common() (+60 more)

### Community 93 - "game/sound: SFXBlock"
Cohesion: 0.03
Nodes (52): SFX, Flags, Grains, InstanceLimit, Pan, UserData, Vol, VolGroup (+44 more)

### Community 94 - "test/decompiler: TEST()"
Cohesion: 0.02
Nodes (3): get_expected(), get_test_data(), TEST()

### Community 95 - "game/graphics: OceanTexture"
Cohesion: 0.04
Nodes (51): OceanTexture, DBUF_SIZE, m_dbuf_a, m_dbuf_b, m_dbuf_x, m_dbuf_y, m_envmap_adgif, m_generate_mipmaps (+43 more)

### Community 96 - "game/graphics: TextureAnimator.cpp"
Cohesion: 0.06
Nodes (33): ClutBlender::ClutBlender(), convert_gs_position_to_vec3(), convert_gs_uv_to_vec2(), debug_save_opengl_texture(), debug_save_opengl_u8_texture(), imgui_show_tex(), interpolate_1(), interpolate_layer_values() (+25 more)

### Community 97 - "decompiler/level_extractor: MercData.cpp"
Cohesion: 0.03
Nodes (67): make_shader(), MercBlendCtrl, blend_vtx_count, bt_index, nonzero_index_count, MercBlendData, u8_data, MercByteHeader (+59 more)

### Community 98 - "goalc/compiler: Val"
Cohesion: 0.09
Nodes (71): Compiler::check_vector_float_regs(), Compiler::compile_asm_add_vf(), Compiler::compile_asm_add_w_vf(), Compiler::compile_asm_add_x_vf(), Compiler::compile_asm_add_y_vf(), Compiler::compile_asm_add_z_vf(), Compiler::compile_asm_break(), Compiler::compile_asm_ftoi_vf() (+63 more)

### Community 99 - "goalc/build_level: ResLump.cpp"
Cohesion: 0.04
Nodes (37): DataObjectGenerator, Res, m_key_frame, m_name, ResFloat, m_values, ResFloat::ResFloat(), ResInt32 (+29 more)

### Community 100 - "game/graphics: DirectRenderer"
Cohesion: 0.06
Nodes (33): DirectRenderer, DirectRenderer::DirectRenderer(), m_blend_state, m_blend_state_needs_gl_update, m_blit_buf_state, m_buffered_tex_state, m_buffered_tex_state_currently_bound, m_current_tex_state_idx (+25 more)

### Community 102 - "game/overlord: jakx/iso_cd.cpp"
Cohesion: 0.04
Nodes (28): CBaseFile, m_Buffer, m_FileDef, m_FileKind, m_LengthPages, m_nNumPages, m_PageOffset, m_ProcessDataSemaphore (+20 more)

### Community 103 - "game/overlord: CDvdDriver"
Cohesion: 0.03
Nodes (51): BlockParams, CDescriptor, m_File, m_pHead, m_pTail, m_status, m_ThreadID, m_unk0 (+43 more)

### Community 104 - "game/sound: MidiHandler"
Cohesion: 0.04
Nodes (34): AmeHandler, MidiError, msg, MidiHandler, m_chanpan, m_chanvol, m_cur_pm, m_get_delta (+26 more)

### Community 105 - "decompiler/data: FakePlayer"
Cohesion: 0.05
Nodes (35): AudioDir, entries, version, AudioFileInfo, filename, length_seconds, Entry, international (+27 more)

### Community 106 - "game/graphics: LoaderInput"
Cohesion: 0.03
Nodes (45): LoaderInput, lev_data, mercs, tex_pool, LoaderStage, m_name, Loader::Loader(), CollideLoaderStage (+37 more)

### Community 107 - "lsp/state: Workspace"
Cohesion: 0.05
Nodes (32): version_to_game_name(), FileType, OpenGOAL, OpenGOALIR, Unsupported, TreeSitterTreeDeleter, Workspace, m_compiler_instances (+24 more)

### Community 108 - "decompiler: Config"
Cohesion: 0.03
Nodes (79): Config, all_types_file, allowed_objects, animated_textures, anon_function_types_by_obj_by_id, apply_patches, art_group_file_override, art_group_info_dump (+71 more)

### Community 109 - "goalc/emitter: Register"
Cohesion: 0.11
Nodes (79): add_f32_f32(), add_gpr64_gpr64_sxtw(), add_vf(), and_gpr64_gpr64(), call_r64(), cmp_f32_f32(), cmp_gpr64_gpr64(), div_f32_f32() (+71 more)

### Community 110 - "goalc/compiler: Util.cpp"
Cohesion: 0.05
Nodes (48): Compiler::ftf_fsf_to_blend_mask(), Compiler::ftf_fsf_to_vector_element(), CompilationOptions, color, disasm_code_only, disassemble, disassembly_output_file, filename (+40 more)

### Community 111 - "goalc/compiler: .get_none()"
Cohesion: 0.07
Nodes (55): Compiler::compile_asm_data_file(), Compiler::compile_asm_file(), Compiler::compile_asm_text_file(), Compiler::compile_autocomplete(), Compiler::compile_build_dgo(), Compiler::compile_bundles(), Compiler::compile_exit(), Compiler::compile_export_requires() (+47 more)

### Community 112 - "game/graphics: CommonOceanRenderer"
Cohesion: 0.05
Nodes (47): Format, DISABLE, IMAGE, PACKED, REGLIST, GifTag, data, reg_descriptor_name() (+39 more)

### Community 113 - "common/util: SmallVector"
Cohesion: 0.07
Nodes (16): Iterator, m_val, operator==(), Range, m_end, m_start, assign(), copy_objects_from_range() (+8 more)

### Community 114 - "decompiler/IR2: FixedOperatorKind"
Cohesion: 0.03
Nodes (78): FixedOperatorKind, ABS, ADDITION, ADDITION_IN_PLACE, ADDITION_PTR, ADDITION_PTR_IN_PLACE, ADDRESS_OF, ARITH_SHIFT (+70 more)

### Community 115 - "decompiler: Top-level CMakeLists.txt"
Cohesion: 0.04
Nodes (75): CMake preset Release-linux-clang-static, CMake preset Release-windows-clang-static, Top-level CMakeLists.txt, build_third_party_lib function, Capstone (Zydis replacement eventually), compile_commands.json copy for clangd, Per-compiler flag setup (Clang, GCC, AppleClang, MSVC), cubeb (audio) (+67 more)

### Community 116 - "goalc/compiler: compilation/Type.cpp"
Cohesion: 0.08
Nodes (41): Compiler::compile_define_state_hook(), Compiler::compile_define_virtual_state_hook(), Compiler::compile_go_hook(), Compiler::compile_state_handler_set(), coerce_to_stack_spill_type(), Compiler::compile_addr_of(), Compiler::compile_car(), Compiler::compile_cast_to_method_type() (+33 more)

### Community 117 - "test: TEST()"
Cohesion: 0.03
Nodes (3): e(), eq(), TEST()

### Community 118 - "common/custom_data: MercModel"
Cohesion: 0.04
Nodes (60): MercModel, effects, max_bones, max_draws, name, st_magic, st_vif_add, xyz_scale (+52 more)

### Community 119 - "decompiler/data: FullGrainInfo"
Cohesion: 0.05
Nodes (61): adpcm_has_loop(), adpcm_sample_size(), compute_sample_rate(), decode_spu_adpcm(), extract_music_bank(), extract_sbk(), extract_sbk_file(), extract_sbk_files() (+53 more)

### Community 120 - "game/graphics: EyeRenderer"
Cohesion: 0.04
Nodes (48): add_clear_draw_to_buffer(), add_draw_to_buffer_32(), add_draw_to_buffer_64(), EyeDraw, scissor, sprite, EyeRenderer, EyeRenderer::EyeDraw::print() (+40 more)

### Community 121 - "decompiler/util: FieldId2"
Cohesion: 0.03
Nodes (74): FieldId2, CPU_FIELDS_END, CPU_FIELDS_START, LAUNCH_FIELDS_END, LAUNCH_FIELDS_START, MISC_FIELDS_END, MISC_FIELDS_START, SPRITE_FIELDS_END (+66 more)

### Community 122 - "common/util: gltf_util.cpp"
Cohesion: 0.06
Nodes (46): affine_rot_qxyzw(), affine_scale(), affine_translation(), colors_from_attribute(), convert_per_vertex_data(), dedup_vertices(), envmap_is_valid(), envmap_settings_from_gltf() (+38 more)

### Community 123 - "decompiler/util: FieldIdX"
Cohesion: 0.03
Nodes (73): FieldIdX, CPU_FIELDS_END, CPU_FIELDS_START, LAUNCH_FIELDS_END, LAUNCH_FIELDS_START, MISC_FIELDS_END, MISC_FIELDS_START, SPRITE_FIELDS_END (+65 more)

### Community 124 - "game/overlord: ISO_VAGCommand"
Cohesion: 0.03
Nodes (66): ISO_VAGCommand, art_flag, clocka, clockb, clockc, clockd, current_spu_address, dma_chan (+58 more)

### Community 125 - "scripts: os"
Cohesion: 0.05
Nodes (27): get_time(), main(), parse_file(), append_file_docs(), get_file_comment(), get_goal_files(), get_goal_files(), lines_in_file() (+19 more)

### Community 126 - "common/repl: Wrapper"
Cohesion: 0.04
Nodes (41): Config, append_keybinds, asm_file_search_dirs, debug_port, game_version, game_version_folder, iso_path, keybinds (+33 more)

### Community 127 - "game/overlord: common/srpc.h"
Cohesion: 0.04
Nodes (64): MusicTweaks, MusicTweak, TweakCount, SoundRpc2SetEarTrans, cam_angle, cam_trans, ear_trans0, ear_trans1 (+56 more)

### Community 128 - "game/overlord: ISO_VAGCommand"
Cohesion: 0.03
Nodes (65): ISO_VAGCommand, art_flag, clocka, clockb, clockc, clockd, current_spu_address, dma_chan (+57 more)

### Community 129 - "decompiler/util: TP_Type"
Cohesion: 0.04
Nodes (17): get_reg_kind(), LoadVarOp::get_src_type(), SimpleAtom::get_type(), get_reg_kind(), get_type_symbol_ptr(), load_var_op_determine_type(), try_get_type_symbol_val(), TP_Type (+9 more)

### Community 130 - "test/offline: Taskfile.yml (root task "
Cohesion: 0.05
Nodes (63): OpenGOAL Modding Hub README (root), Consolidated launcher mod catalog index.json, In-game Mods menu (L3 + SELECT), Player install flow via OpenGOAL Launcher (add catalog, install, play, toggle), Branch model: master mirrors upstream, master-dev is the modding base, opengoal-modding-kb knowledge base (Lisp wiki at .agents/skills), One repository per mod (<game>-mod-<name>) created from master-dev, sync-upstream.yaml daily workflow (upstream -> master -> master-dev) (+55 more)

### Community 131 - "game/system: DisplayManager"
Cohesion: 0.05
Nodes (28): DisplayManager, DisplayManager::DisplayManager(), ee_event_queue, event_queue_mtx, m_available_resolutions, m_available_window_sizes, m_current_display_modes, m_display_settings (+20 more)

### Community 132 - "game/graphics: PrimBuildState"
Cohesion: 0.03
Nodes (58): BlendState, a, alpha_blend_enable, b, c, current_register, d, fix (+50 more)

### Community 133 - "decompiler/types2: SimpleExpression"
Cohesion: 0.18
Nodes (55): SimpleExpression, m_args, m_kind, n_args, AsmBranchOp::propagate_types2(), AsmOp::propagate_types2(), backprop_tagged_type(), branch_delay_types2() (+47 more)

### Community 134 - "decompiler/util: FieldId"
Cohesion: 0.03
Nodes (69): FieldId, CPU_FIELDS_END, CPU_FIELDS_START, LAUNCH_FIELDS_END, LAUNCH_FIELDS_START, MISC_FIELDS_END, MISC_FIELDS_START, SPRITE_FIELDS_END (+61 more)

### Community 135 - "game/graphics: Shadow2"
Cohesion: 0.05
Nodes (44): CameraMatrix, v, FrameConstants, camera, constants, mystery, InputData, bottom_vertex_data (+36 more)

### Community 136 - "goalc/build_level: LevelFile"
Cohesion: 0.04
Nodes (53): BspNode, CityLevelInfo, DrawableTreeActor, DrawableTreeArray, actors, regions, shrubs, tfrags (+45 more)

### Community 137 - "goalc/emitter: InstructionX86"
Cohesion: 0.06
Nodes (57): cdq(), load16s_gpr64_gpr64_plus_gpr64(), load16s_gpr64_gpr64_plus_gpr64_plus_s32(), load16s_gpr64_gpr64_plus_gpr64_plus_s8(), load16u_gpr64_gpr64_plus_gpr64(), load16u_gpr64_gpr64_plus_gpr64_plus_s32(), load16u_gpr64_gpr64_plus_gpr64_plus_s8(), load32s_gpr64_gpr64_plus_gpr64() (+49 more)

### Community 138 - "game/overlord: jak3/streamlist.cpp"
Cohesion: 0.05
Nodes (47): Init(), PluginOp, Queue, SetVol, Stop, StopAll, PluginStreamOps, wakeup_thread (+39 more)

### Community 139 - "goalc/build_level: LevelFile"
Cohesion: 0.04
Nodes (52): BspNode, CityLevelInfo, DrawableTreeActor, DrawableTreeArray, actors, shrubs, tfrags, ties (+44 more)

### Community 140 - "goalc/regalloc: VarAssignment"
Cohesion: 0.08
Nodes (40): allocate_registers_v2(), AssignmentOrder, gprs, simds, AssignmentSettings, only_move_eliminate_assigns, prefer_saved, trace_debug (+32 more)

### Community 141 - "common/formatter: FormatterTreeNode"
Cohesion: 0.05
Nodes (39): apply_formatting(), can_node_be_inlined(), form_contains_comment(), form_contains_node_that_prevents_inlining(), formatter::format_code(), get_total_form_inlined_width(), hang_indentation_width(), join_formatted_lines() (+31 more)

### Community 142 - "decompiler/data: game_text.cpp"
Cohesion: 0.04
Nodes (36): append(), build_list(), float_representation(), new_string(), to_symbol(), font_bank_exists(), Kind, IMAGE (+28 more)

### Community 143 - "common/log: log.cpp"
Cohesion: 0.04
Nodes (43): debug(), die(), error(), info(), level, debug, die, error (+35 more)

### Community 144 - "game/sound: VoiceManager"
Cohesion: 0.04
Nodes (38): PitchBend(), PS1Note2Pitch(), sceSdNote2Pitch(), Tone, ADSR1, ADSR2, CenterFine, CenterNote (+30 more)

### Community 145 - "common/util: GameTextFontBank"
Cohesion: 0.05
Nodes (38): Format, GOAL, JSON, GameTextDefinitionFile, file_path, format, group_name, language_id (+30 more)

### Community 146 - "decompiler/IR2: AtomicOp.h"
Cohesion: 0.03
Nodes (32): AsmBranchOp, AsmBranchOp::AsmBranchOp(), m_branch_delay, m_branch_delay_sp, m_condition, m_label, m_likely, BranchOp (+24 more)

### Community 147 - "decompiler/level_extractor: TFragment"
Cohesion: 0.03
Nodes (56): HFragment, colors, kCornersPerEdge, kNumCorners, kNumVerts, kVertsPerEdge, montage, num_buckets_far (+48 more)

### Community 148 - "decompiler/level_extractor: array"
Cohesion: 0.06
Nodes (52): debug_dump_proto_to_obj(), DrawSettings, combo_tex, mode, dump_full_to_obj(), extract_instance(), extract_proto(), extract_shrub() (+44 more)

### Community 149 - "game/sound: BlockSoundHandler"
Cohesion: 0.04
Nodes (37): BlockSoundHandler, BlockSoundHandler::BlockSoundHandler(), m_app_pan, m_app_pb, m_app_pm, m_app_volume, m_children, m_countdown (+29 more)

### Community 150 - "goalc/make: Tools.cpp"
Cohesion: 0.07
Nodes (15): open_subtitle_project(), PathMap, output_prefix, path_remap, ToolInput, arg, BuildLevel2Tool, BuildLevel3Tool (+7 more)

### Community 151 - "goalc/build_level: LevelFile"
Cohesion: 0.04
Nodes (44): DataObjectGenerator, DrawableTreeAmbient, AdgifShaderArray, adgifs, Box8s, BspNode, DrawableInlineArrayAmbient, ambients (+36 more)

### Community 152 - "common/goos: Reader.cpp"
Cohesion: 0.08
Nodes (26): decimal_start(), float_start(), get_byte_string(), get_readable_string(), hex_char(), ListBuilder, head, prev_tail (+18 more)

### Community 153 - "common/util: json"
Cohesion: 0.04
Nodes (27): align16(), align2(), align32(), align4(), align64(), align8(), get_bit_range(), get_power_of_two() (+19 more)

### Community 154 - "goalc/emitter: ARM64_REG"
Cohesion: 0.03
Nodes (65): ARM64_REG, SP, V0, V1, V10, V11, V12, V13 (+57 more)

### Community 155 - "decompiler/analysis: cfg_builder.cpp"
Cohesion: 0.11
Nodes (44): build_initial_forms(), cfg_to_ir(), cfg_to_ir_allow_null(), cfg_to_ir_helper(), clean_up_break(), clean_up_break_final(), clean_up_cond_no_else(), clean_up_cond_no_else_final() (+36 more)

### Community 156 - "goalc/build_level: jak3/collide.cpp"
Cohesion: 0.07
Nodes (48): CollideFace, bsphere, pat, v, add_all_to_frag(), add_pod_to_object_file(), add_pod_vector_to_object_file(), add_to_object_file() (+40 more)

### Community 157 - "goalc/build_level: tfrag3data"
Cohesion: 0.04
Nodes (23): ObjectFileData, clean_up_vertex_indices(), GPUTestOutput, error, errorCause, gpuRendererString, gpuVendorString, success (+15 more)

### Community 158 - "game/graphics: Hfrag"
Cohesion: 0.05
Nodes (35): Hfrag, Hfrag::Hfrag(), kIndsPerTile, kMaxLevels, kNumBuckets, kNumCorners, kNumMontageTiles, m_bucket_used (+27 more)

### Community 159 - "decompiler/extractor: parse_commented_json()"
Cohesion: 0.05
Nodes (36): parse_commented_json(), parse_json_optional_integer_range(), strip_cpp_style_comments(), from_json(), make_config_via_json(), read_config_file(), read_json_file_from_config(), to_json() (+28 more)

### Community 160 - "decompiler/Disasm: InstructionAtom"
Cohesion: 0.06
Nodes (18): DecompilerLabel, Instruction, cop2_bc, cop2_dest, dst, il, kind, n_dst (+10 more)

### Community 161 - "game/system: pair"
Cohesion: 0.05
Nodes (38): pair, ButtonIndex, CIRCLE, CROSS, DPAD_DOWN, DPAD_LEFT, DPAD_RIGHT, DPAD_UP (+30 more)

### Community 162 - "game/graphics: PcTextureAnimCodesJak3"
Cohesion: 0.03
Nodes (61): PcTextureAnimCodesJak3, CLOUDS_AND_FOG, CLOUDS_HIRES, COMB_FIELD, CTYSLUMB_WATER, CTYSLUMC_WATER, DARKJAK, DARKJAK_HIGHRES (+53 more)

### Community 163 - "game/system: SystemThread"
Cohesion: 0.04
Nodes (34): deci2_runner(), ee_worker_runner(), null_runner(), SystemThread, cpu_kernel, cpu_user, id, initialization_complete (+26 more)

### Community 164 - "goalc/emitter: InstructionARM64"
Cohesion: 0.08
Nodes (49): add_gpr64_imm(), add_gpr64_imm32s(), add_gpr64_imm8s(), can_encode_single_imm12(), cdq(), decompose_into_imm12_chunks(), decompose_into_imm16_chunks(), dup_vf_lane() (+41 more)

### Community 165 - "goalc/regalloc: AllocationInput"
Cohesion: 0.06
Nodes (48): allocate_registers(), analyze_liveliness(), assign_var_no_check(), assignment_ok_at(), can_var_be_assigned(), check_constrained_alloc(), compute_live_ranges(), do_allocation_for_var() (+40 more)

### Community 166 - "decompiler/analysis: PrettyPrinter"
Cohesion: 0.04
Nodes (14): convert_to_expressions(), DecompilerTypeSystem, Form, FormPool, Function, rewrite_inline_asm_instructions(), insert_static_refs(), kind_for_lambda() (+6 more)

### Community 167 - "game/graphics: opengl.cpp"
Cohesion: 0.05
Nodes (24): scoped_prof(), ScopedEvent, prof, GfxDisplay, m_imgui_visible, m_main, Loop(), gl_exit() (+16 more)

### Community 168 - "decompiler/IR2: GenericOperator"
Cohesion: 0.04
Nodes (36): GenericElement::GenericElement(), GenericOperator, m_condition_kind, m_fixed_kind, m_function, m_kind, Kind, AND (+28 more)

### Community 169 - "decompiler/types2: Instruction"
Cohesion: 0.04
Nodes (51): AmbiguousIntOrFloatConstant, is_float, Block, block_entry_tags, instructions, needs_run, start_type_state, start_types (+43 more)

### Community 170 - "game/sound: SoundHandler"
Cohesion: 0.04
Nodes (24): SoundHandler, m_sound_handle, BankTag, BankID, DataID, Flags, Version, BlockFlags (+16 more)

### Community 171 - "tools: vendor.yaml (third-party"
Cohesion: 0.04
Nodes (57): Sublime Text GOAL setup notes, goal.sublime-syntax syntax highlighting, lispindent plugin formatting for GOAL, task analyze-ee-memory / watch-pcsx2 (memory_dump_tool on savestates), task format-gsrc (formatter binary on a gsrc file), task type-test / tests-filtered (goalc-test gtest filter), task type-search (type_searcher example), task unit-tests (goalc-test) (+49 more)

### Community 172 - "game/graphics: GfxGlobalSettings"
Cohesion: 0.04
Nodes (56): CollisionRendererClearMask(), CollisionRendererGetMask(), CollisionRendererMode, Event, Material, Mode, None, Skip (+48 more)

### Community 173 - "game/settings: InputSettings"
Cohesion: 0.04
Nodes (44): DebugSettings, alternate_style, current_version, hide_imgui_key, ignore_hide_imgui, imgui_font_scale, monospaced_font, show_imgui (+36 more)

### Community 174 - "common/cross_os_debug: xdbg.cpp"
Cohesion: 0.06
Nodes (31): attach_and_break(), break_now(), check_stopped(), close_memory(), cont_now(), DebugContext, base, s7 (+23 more)

### Community 175 - "common/custom_data: TFrag3Data.cpp"
Cohesion: 0.06
Nodes (48): Blerc::serialize(), BVH::serialize(), CollisionMesh::memory_usage(), CollisionMesh::serialize(), Hfragment::memory_usage(), Hfragment::serialize(), HfragmentBucket::serialize(), IndexTexture::memory_usage() (+40 more)

### Community 176 - "game/graphics: OceanEnvmap"
Cohesion: 0.06
Nodes (24): find_sky_color(), is_untextured_draw(), make_single_level_linear(), OceanEnvmap, ENVMAP_HEIGHT, ENVMAP_VRAM_ADDR, ENVMAP_WIDTH, m_envmap_fb (+16 more)

### Community 177 - "game/sound: Player"
Cohesion: 0.07
Nodes (11): Player, mCtx, mHandleAllocator, mHandlers, mLoader, mStream, mSynth, mTick (+3 more)

### Community 178 - "game/graphics: Loader"
Cohesion: 0.06
Nodes (26): Loader, m_active_levels, m_all_merc_models, m_base_path, m_common_level, m_desired_levels, m_file_load_done_cv, m_garbage_buffers (+18 more)

### Community 179 - "goalc/build_level: jak2/collide.cpp"
Cohesion: 0.07
Nodes (43): add_all_to_frag(), add_pod_to_object_file(), add_pod_vector_to_object_file(), add_to_object_file(), BBoxBuilder, added_one, box, bounding_box_bounding_box() (+35 more)

### Community 180 - "goalc/emitter: RegisterInfo"
Cohesion: 0.05
Nodes (33): hash, HWRegKind, GPR, INVALID, SIMD, reg_class_to_hw(), Register, m_id (+25 more)

### Community 181 - "game/graphics: ShadowRenderer"
Cohesion: 0.05
Nodes (30): clip(), fcand(), fsand(), ShadowRenderer::handle_jalr_to_end_block(), ShadowRenderer::run_mscal10_vu2c(), ShadowRenderer::run_mscal_vu2c(), ShadowRenderer, m_back_indices (+22 more)

### Community 182 - "game/graphics: OpenGlDebugGui"
Cohesion: 0.04
Nodes (36): DmaStats, num_chunks, num_copied_bytes, num_data_bytes, num_fixups, num_tags, sync_time_ms, FrameTimeRecorder (+28 more)

### Community 183 - "decompiler/IR2: FormStack.cpp"
Cohesion: 0.07
Nodes (27): same_expression_var(), can_inline_non_seq_source(), Form, FormStack, m_is_root_stack, m_stack, FormStack::StackEntry::print(), is_op_in_place() (+19 more)

### Community 184 - "decompiler/IR2: function"
Cohesion: 0.04
Nodes (20): DefpartgroupElement, m_group_id, m_static_info, MethodOfTypeElement, m_method_info, m_type_at_decompile, m_type_reg, SimpleAtomElement (+12 more)

### Community 185 - "game/graphics: Shrub"
Cohesion: 0.04
Nodes (35): Cache, draw_idx_temp, index_temp, multidraw_count_buffer, multidraw_index_offset_buffer, multidraw_offset_per_stripdraw, Shrub, m_cache (+27 more)

### Community 186 - "common/global_profiler: GlobalProfiler"
Cohesion: 0.05
Nodes (23): get_current_tid(), get_current_ts(), GlobalProfiler, GlobalProfiler::GlobalProfiler(), m_enable_compression, m_enabled, m_ignore_events, m_max_events (+15 more)

### Community 187 - "common/util: path"
Cohesion: 0.08
Nodes (43): base_name(), base_name_no_ext(), combine_path(), convert_to_unix_path_separators(), copy_file(), create_dir_if_needed(), create_dir_if_needed_for_file(), decompress_dgo() (+35 more)

### Community 188 - "goalc/make: MakeSystem"
Cohesion: 0.08
Nodes (17): MakeStep, arg, deps, input, outputs, tool, MakeSystem, m_goos (+9 more)

### Community 189 - "decompiler/IR2: Entry"
Cohesion: 0.04
Nodes (37): DefskelgroupElement, m_info, m_name, m_static_info, DefstateElement, m_entries, m_is_override, m_is_virtual (+29 more)

### Community 190 - "decompiler/level_extractor: MercCtrlHeader"
Cohesion: 0.04
Nodes (51): MercCtrlHeader, blend_target_count, cross_copy_count, death_effect, death_start_vertex, death_vertex_skip, display_this_fragment, display_triangles (+43 more)

### Community 191 - ".github/workflows: AGENTS.md agent guide (O"
Cohesion: 0.05
Nodes (49): Mod Bug Report issue template, Install method field (Launcher, debug build, manual zip), OpenGOAL Launcher, Mod Version field (release tag or commit hash), Bug report form fields (game, steps, attachments, environment), Upstream open-goal/jak-project issue tracker, Mod Suggestion issue template, Mod Category dropdown (six categories) (+41 more)

### Community 192 - "goalc/build_level: ResLump"
Cohesion: 0.06
Nodes (31): ResLump, m_res, m_sorted, EntityActor, aid, bsphere, etype, game_task (+23 more)

### Community 193 - "common/dma: GsRegisterAddress"
Cohesion: 0.04
Nodes (55): GsRegisterAddress, ALPHA_1, ALPHA_2, BITBLTBUF, CLAMP_1, CLAMP_2, COLCLAMP, DIMX (+47 more)

### Community 194 - "game/kernel: SpeedrunPracticeObjectiv"
Cohesion: 0.04
Nodes (51): AutoSplitterBlock, marker, pointer_to_symbol, DiscordInfo, active_gun, current_vehicle, cutscene, death_count (+43 more)

### Community 195 - "game/sound: Voice"
Cohesion: 0.05
Nodes (21): AllocationType, Managed, Permanent, ApplyVolume(), Voice, mADSR, mAlloc, mCounter (+13 more)

### Community 196 - "game/graphics: OceanMid"
Cohesion: 0.06
Nodes (20): DmaTag, addr, kind, qwc, spr, emulate_dma(), is_end_tag(), OceanMid (+12 more)

### Community 197 - "common/goos: InternedSymbolPtr"
Cohesion: 0.06
Nodes (24): Interpreter::Interpreter(), Entry, hash, key, name, value, hash, InternedPtrMap (+16 more)

### Community 198 - "game/graphics: Warp"
Cohesion: 0.04
Nodes (20): Generic2BucketRenderer, Generic2BucketRenderer::Generic2BucketRenderer(), m_empty, m_generic, m_mode, bitcount(), LevelStats, has_vis (+12 more)

### Community 200 - "game/kernel: PickupType"
Cohesion: 0.04
Nodes (53): PickupType, ammo_blue, ammo_dark, ammo_dark_light_random, ammo_light_random, ammo_random, ammo_red, ammo_yellow (+45 more)

### Community 201 - "game/overlord: Jak2SoundCommand"
Cohesion: 0.04
Nodes (53): Jak2SoundCommand, boot_load, cancel_dgo, continue_group, continue_sound, game_load, get_irx_version, iop_free (+45 more)

### Community 202 - "goalc/emitter: IGenX86.cpp"
Cohesion: 0.10
Nodes (49): add_f32_f32(), add_gpr64_gpr64(), add_gpr64_imm(), add_gpr64_imm32s(), add_gpr64_imm8s(), and_gpr64_gpr64(), cmp_f32_f32(), cmp_gpr64_gpr64() (+41 more)

### Community 203 - "common/type_system: Type"
Cohesion: 0.04
Nodes (26): MethodInfo, defined_in_type, docstring, id, name, no_virtual, only_overrides_docstring, overlay_name (+18 more)

### Community 204 - "decompiler/data: TexturePage"
Cohesion: 0.07
Nodes (40): FileInfo, file_name, file_type, major_version, maya_file_name, mdb_file_name, minor_version, tool_debug (+32 more)

### Community 205 - "game/graphics: Vu"
Cohesion: 0.04
Nodes (51): Vu, acc, P, Q, vf00, vf01, vf02, vf03 (+43 more)

### Community 206 - "game/graphics: FramebufferTexturePair"
Cohesion: 0.06
Nodes (23): FramebufferCopier, m_fbo, m_fbo_height, m_fbo_texture, m_fbo_width, FramebufferTexturePair, m_framebuffers, m_h (+15 more)

### Community 207 - "goalc/build_level: PatSurface"
Cohesion: 0.06
Nodes (14): CollideVertex, x, y, z, jak2_pat(), jak3_pat(), Mode, GROUND (+6 more)

### Community 208 - "goalc/build_level: color_quantization.cpp"
Cohesion: 0.09
Nodes (41): assign_colors(), child_index(), collapse1(), collapse_as_needed(), collapse_at_level(), color_difference(), color_less_than(), color_rgb() (+33 more)

### Community 209 - "decompiler/util: DecompilerTypeSystem"
Cohesion: 0.06
Nodes (22): cdr(), DecompilerTypeSystem, art_group_info, bad_format_strings, DecompilerTypeSystem::DecompilerTypeSystem(), format_ops_with_dynamic_string_by_func_name, jg_info, m_reader (+14 more)

### Community 210 - "decompiler/IR2: Env"
Cohesion: 0.05
Nodes (14): get_condition_kind_name(), load_kind_to_string(), AsmBranchElement, m_branch_delay, m_branch_op, m_likely, AsmOpElement, m_op (+6 more)

### Community 211 - "decompiler/IR2: DerefToken"
Cohesion: 0.04
Nodes (16): DerefElement, DerefElement::DerefElement(), m_base, m_is_addr_of, m_tokens, DerefToken, m_expr, m_int_constant (+8 more)

### Community 212 - "game/graphics: Tree"
Cohesion: 0.04
Nodes (44): CommonData, envmap_color, frame_idx, proto_vis_data, proto_vis_data_size, settings, TieProtoVisibility, all_visible (+36 more)

### Community 213 - "game/graphics: BlitDisplays"
Cohesion: 0.06
Nodes (26): BlitDisplays, BlitDisplays::BlitDisplays(), m_blur_new_copier, m_blur_old_copier, m_color_draw, m_color_filter, m_color_filter_pending, m_copier (+18 more)

### Community 214 - "game/graphics: Vu"
Cohesion: 0.04
Nodes (50): Vu, acc, P, Q, vf00, vf01, vf02, vf03 (+42 more)

### Community 215 - "game/graphics: TextureAnimator.h"
Cohesion: 0.04
Nodes (45): ClutReader, addrs, DynamicLayerData, end_vals, start_vals, FixedAnim, def, dest_slot (+37 more)

### Community 216 - "game/sound: MIDISound"
Cohesion: 0.05
Nodes (42): midi_voice, channel, note, velocity, Midi, BankID, DataID, DataStart (+34 more)

### Community 217 - "game/tools: SubtitleEditor"
Cohesion: 0.06
Nodes (29): SubtitleEditor, m_current_language, m_current_scene, m_current_scene_frames, m_current_scene_merge, m_current_scene_offscreen, m_current_scene_speaker, m_current_scene_text (+21 more)

### Community 218 - "goalc/debugger: Debugger"
Cohesion: 0.04
Nodes (37): Debugger, INSTR_DUMP_SIZE_FWD, INSTR_DUMP_SIZE_REV, m_addr_breakpoints, m_attach_cv, m_attach_response, m_attach_return, m_attached (+29 more)

### Community 219 - "game/sound: ADSR"
Cohesion: 0.06
Nodes (23): ADSR, m_Phase, m_Reg, m_Target, Envelope, m_Counter, m_Decrease, m_Exp (+15 more)

### Community 220 - "decompiler/ObjectFile: ObjectFileDB_IR2.cpp"
Cohesion: 0.08
Nodes (28): find_blocks_in_function(), for_each_function_in_seg_in_obj(), append_commented(), find_file_override_for_art_group(), ObjectFileDB::analyze_functions_ir2(), ObjectFileDB::ir2_add_store_errors(), ObjectFileDB::ir2_atomic_op_pass(), ObjectFileDB::ir2_basic_block_pass() (+20 more)

### Community 221 - "common/math: Vector"
Cohesion: 0.09
Nodes (7): cast(), head(), Matrix, m_data, operator*(), Vector, m_data

### Community 222 - "decompiler/util: sparticle_decompile.cpp"
Cohesion: 0.14
Nodes (37): degrees_to_string(), fixed_point_to_float(), fixed_point_to_string(), float_to_cstr(), float_to_string(), meters_to_string(), proper_float(), seconds_to_string() (+29 more)

### Community 223 - "decompiler/Disasm: OpcodeFields"
Cohesion: 0.13
Nodes (23): decode_BC1(), decode_c0(), decode_cache(), decode_cop0(), decode_cop1(), decode_cop2(), decode_instruction(), decode_mf0() (+15 more)

### Community 224 - "game/graphics: Merc2"
Cohesion: 0.04
Nodes (48): DrawFlags, IGNORE_ALPHA, MOD_VTX, NO_TEXTURE, Merc2, BONE_VECTORS_PER_BONE, kMaxBlerc, kMaxEffect (+40 more)

### Community 225 - "game/graphics: ClutBlender"
Cohesion: 0.04
Nodes (41): ClutBlender, m_cluts, m_current_weights, m_dest, m_temp_clut, m_temp_rgba, m_texture, pool_gpu_tex (+33 more)

### Community 226 - "goalc/emitter: s64"
Cohesion: 0.16
Nodes (49): add_gpr64_gpr64(), construct_multiple_imm12_adds(), construct_multiple_imm12_subs(), lea_reg_plus_off(), lea_reg_plus_off32(), lea_reg_plus_off8(), load128_simd128_gpr64(), load128_simd128_gpr64_s32() (+41 more)

### Community 227 - "scripts/modding: update_mod_catalog.py"
Cohesion: 0.07
Nodes (25): default_remote(), drop_path(), ensure_remote(), find_repo_root(), get_current_branch(), git_quiet(), is_ancestor(), is_working_tree_clean() (+17 more)

### Community 228 - "goalc/emitter: TEST()"
Cohesion: 0.05
Nodes (7): execute_tester(), TEST(), emit_div_sequence(), run_mem(), TEST(), VecMem, buf

### Community 229 - "game/sound: AmeHandler"
Cohesion: 0.06
Nodes (20): AMEError, msg, AmeHandler, AmeHandler::AmeHandler(), m_groups, m_header, m_macro, m_midis (+12 more)

### Community 230 - "common/goos: PrettyPrinterNode"
Cohesion: 0.09
Nodes (40): add_to_token_list(), breakList(), FormToken, kind, str, get_case_start_case(), getFirstBadLine(), getFirstListOnLine() (+32 more)

### Community 231 - "game/sound: BinaryReader"
Cohesion: 0.07
Nodes (24): BinaryReader, m_seek, m_span, chunk, bank, midi, samples, FileAttributes (+16 more)

### Community 232 - "game/graphics: Vu"
Cohesion: 0.04
Nodes (48): Vu, acc, Q, vf00, vf01, vf02, vf03, vf04 (+40 more)

### Community 233 - "game/graphics: FixedLayerDef"
Cohesion: 0.05
Nodes (39): FixedAnimDef, color, layers, move_to_pool, override_size, set_alpha, tex_name, FixedLayerDef (+31 more)

### Community 234 - "game/overlord: jak3/iso_cd.cpp"
Cohesion: 0.07
Nodes (12): get_driver(), CISOCDFile, CISOCDFile::CISOCDFile(), m_Descriptor, m_nLength, m_nLoaded, m_nSector, CISOCDFileSystem (+4 more)

### Community 235 - "goalc/build_level: CollideFragMeshData"
Cohesion: 0.06
Nodes (35): CollideFrag, bsphere, faces, DrawableInlineArrayCollideFrag, frags, DrawableInlineArrayNode, nodes, DrawNode (+27 more)

### Community 236 - "decompiler/data: TextureDB"
Cohesion: 0.06
Nodes (27): ResolvedTextureData, h, rgba, w, TexInfo, idx, name, tpage_name (+19 more)

### Community 237 - "decompiler/IR2: SetFormFormElement"
Cohesion: 0.04
Nodes (20): SetFormFormElement, m_cast_for_define, m_cast_for_set, m_dst, m_real_push_count, m_src, StackSpillValueElement, m_access (+12 more)

### Community 238 - "test/goalc: ArithmeticTests"
Cohesion: 0.07
Nodes (17): uri_from_path(), uri_to_path(), url_decode(), url_encode(), LSPRequester, ArithmeticTests, compiler, env (+9 more)

### Community 239 - "game/graphics: DepthCue"
Cohesion: 0.06
Nodes (30): DepthCue, DepthCue::DepthCue(), m_debug, m_draw_slices, m_gs_restore, m_gs_setup, m_ogl, DepthCuePageDraw (+22 more)

### Community 240 - "game/mips2c: Cache"
Cohesion: 0.04
Nodes (35): Cache, clip_polygon_against_negative_hyperplane, clip_polygon_against_positive_hyperplane, draw_boundary_polygon, fake_scratchpad_data, math_camera, sky_work, execute() (+27 more)

### Community 241 - "game/overlord: VagCmd"
Cohesion: 0.04
Nodes (45): VagCmd, dma_chan, dma_iop_mem_ptr, file_record, fo_curve, fo_max, fo_min, header (+37 more)

### Community 242 - "game/system: MouseDevice"
Cohesion: 0.05
Nodes (26): ActiveMouseAction, binding, player_movement, revert_action, sdl_mouse_button, MouseButtonStatus, left, middle (+18 more)

### Community 243 - "goalc/emitter: Register"
Cohesion: 0.09
Nodes (45): add_vf(), blend_vf(), div_vf(), ftoi_vf(), itof_vf(), max_vf(), min_vf(), mov_vf_vf() (+37 more)

### Community 244 - "common/dma: GsTest"
Cohesion: 0.06
Nodes (35): AlphaFail, FB_ONLY, KEEP, RGB_ONLY, ZB_ONLY, AlphaTest, ALWAYS, EQUAL (+27 more)

### Community 245 - "decompiler/IR2: SimpleAtom"
Cohesion: 0.05
Nodes (15): SimpleAtom, m_display_int_as_float, m_int, m_kind, m_no_display_int_as_hex, m_string, m_variable, StackSpillStoreOp::StackSpillStoreOp() (+7 more)

### Community 246 - "game/graphics: ShaderId"
Cohesion: 0.04
Nodes (47): ShaderId, COLLISION, DEBUG_RED, DEPTH_CUE, DIRECT2, DIRECT_BASIC, DIRECT_BASIC_TEXTURED, DIRECT_BASIC_TEXTURED_MULTI_UNIT (+39 more)

### Community 247 - "game/graphics: GlowRenderer"
Cohesion: 0.11
Nodes (20): copy_to_vertex(), GlowRenderer, kDownsampleBatchWidth, kDownsampleIterations, kFirstDownsampleSize, kMaxIndices, kMaxSprites, kMaxVertices (+12 more)

### Community 248 - "goalc/compiler: .for_each_in_list()"
Cohesion: 0.09
Nodes (24): Compiler::compile_begin(), Compiler::compile_block(), Compiler::compile_goto(), Compiler::compile_label(), Compiler::compile_nop(), Compiler::compile_return_from(), Compiler::compile_top_level(), Compiler::compile_and_or() (+16 more)

### Community 249 - "decompiler/Disasm: .parse_single_instructio"
Cohesion: 0.07
Nodes (22): DecompilerLabel, name, offset, target_segment, cop2_dst(), get_before_paren(), get_comma_separated(), get_in_paren() (+14 more)

### Community 250 - "game/kernel: jak2/kmachine_extras.cpp"
Cohesion: 0.10
Nodes (36): get_font_bank(), safe_parse_json(), alloc_vagdir_names(), bool_to_symbol(), callback_fetch_external_highscores(), callback_fetch_external_race_times(), callback_fetch_external_speedrun_times(), init_autosplit_struct() (+28 more)

### Community 251 - "common/serialization: GameSubtitleBank"
Cohesion: 0.06
Nodes (25): GameSubtitleBank, m_base_scenes, m_file_base_path, m_file_path, m_lang_id, m_scenes, m_speakers, m_text_version (+17 more)

### Community 252 - "decompiler/IR2: form_as_atom()"
Cohesion: 0.10
Nodes (26): get_cloth_params(), get_skelgroup_name(), inspect_cloth_data_jak3(), inspect_skel_group_data_jak1(), inspect_skel_group_data_jak2(), inspect_skel_group_data_jak3(), rewrite_defskelgroup(), run_defskelgroups() (+18 more)

### Community 253 - "goalc/debugger: FunctionDebugInfo"
Cohesion: 0.06
Nodes (31): DebugInfo, DebugInfo::DebugInfo(), m_functions, m_obj_name, FunctionDebugInfo, code_sources, generated_code, instructions (+23 more)

### Community 254 - "goalc/emitter: emitter/Instruction.h"
Cohesion: 0.10
Nodes (38): blend_vf(), ins_vf_lane(), ins_vf_lane_h(), mov_gpr32_link_imm32(), mov_vf_vf(), ph_sll(), ph_srl(), pw_sll() (+30 more)

### Community 255 - "game/sound: Grain"
Cohesion: 0.15
Nodes (5): Grain, data, Delay, func, Type

### Community 256 - "decompiler/IR2: Kind"
Cohesion: 0.04
Nodes (45): Kind, ANY, ANY_CONSTANT_TOKEN, ANY_EXPR, ANY_EXPR_OR_INT, ANY_FLOAT, ANY_INT, ANY_INTEGER (+37 more)

### Community 257 - "game/graphics: OceanNear"
Cohesion: 0.07
Nodes (12): is_end_tag(), OceanNear, m_buffer_toggle, m_common_ocean_renderer, m_texture_renderer, m_vu_data, OceanNear::OceanNear(), vu (+4 more)

### Community 258 - "game/sound: LFOTracker"
Cohesion: 0.05
Nodes (32): BlockSoundHandler, LFOTarget, NONE, PAN, PBEND, PMOD, UNK1, UNK2 (+24 more)

### Community 259 - "common/custom_data: TfragTree"
Cohesion: 0.05
Nodes (34): pack_tfrag_vertices(), position_to_cluster_and_offset(), BVH, first_leaf_node, first_root, last_leaf_node, num_roots, only_children (+26 more)

### Community 260 - "decompiler/level_extractor: tfrag_tie_fixup.cpp"
Cohesion: 0.09
Nodes (34): apply_flips(), bfs_order_connected_component(), build_graph(), compute_flips(), ConnectedComponent, groups, find_connected_components(), fixup_and_unstrip_tfrag_tie() (+26 more)

### Community 261 - ".github/workflows: Build & Release OpenGOAL"
Cohesion: 0.08
Nodes (40): Build Check workflow (on-demand compile check), build-check binary artifacts (3-day retention), authorize job (repository owner gate), build-linux job (Clang static), sccache compiler cache, extractor build target, gk build target (game runtime), goalc build target (GOAL compiler) (+32 more)

### Community 262 - "common/type_system: TypeFieldLookup.cpp"
Cohesion: 0.08
Nodes (34): deref_matches(), FieldReverseLookupOutput::Token::print(), parent_to_vector(), ReverseLookupNode::to_vector(), try_reverse_lookup(), try_reverse_lookup_array_like(), try_reverse_lookup_inline_array(), try_reverse_lookup_other() (+26 more)

### Community 263 - "decompiler/analysis: string"
Cohesion: 0.20
Nodes (38): dest_to_char(), handle_ceqs(), handle_cfc2(), handle_cles(), handle_clts(), handle_ctc2(), handle_div_divu(), handle_generic_load() (+30 more)

### Community 264 - "decompiler/level_extractor: Ref"
Cohesion: 0.07
Nodes (25): CollideFragMesh, base_trans, packed_data, pat_array, poly_count, strip_data_len, total_qwc, vertex_count (+17 more)

### Community 265 - "game/mips2c: VfName"
Cohesion: 0.05
Nodes (43): VfName, vf0, vf00, vf01, vf02, vf03, vf04, vf05 (+35 more)

### Community 266 - "goalc/data_compiler: DataObjectGenerator"
Cohesion: 0.12
Nodes (9): add_data_to_vector(), DataObjectGenerator, m_ptr_links, m_string_pool, m_symbol_links, m_type_links, m_words, push_better_variable_length_integer() (+1 more)

### Community 267 - "goalc/regalloc: RegAllocBasicBlock"
Cohesion: 0.08
Nodes (23): ControlFlowAnalysisCache, basic_blocks, find_basic_blocks(), print_allocate_input(), print_result(), RegAllocBasicBlock, dead, defs (+15 more)

### Community 268 - "game/sce: sif_ee_memcard.cpp"
Cohesion: 0.09
Nodes (33): MC_makefile(), CardData, files, is_formatted, File, data, is_directory, flush_memory_card_to_file() (+25 more)

### Community 269 - "decompiler/ObjectFile: LinkedObjectFileCreation"
Cohesion: 0.08
Nodes (37): assert_string_empty_after(), c_symlink2(), c_symlink3(), DecompilerTypeSystem, link_v2_or_v4(), link_v3(), link_v5(), LinkHeaderCommon (+29 more)

### Community 270 - "decompiler/types2: types2.cpp"
Cohesion: 0.09
Nodes (23): backprop_from_preds(), build_function(), Cast, is_reg, previous, reg, stack_slot, construct_function_entry_types() (+15 more)

### Community 271 - "game/kernel: jak3/kmachine_extras.cpp"
Cohesion: 0.11
Nodes (35): alloc_vagdir_names(), bool_to_symbol(), callback_fetch_external_highscores(), callback_fetch_external_race_times(), callback_fetch_external_speedrun_times(), init_autosplit_struct(), pc_fetch_external_highscores(), pc_fetch_external_race_times() (+27 more)

### Community 272 - "game/kernel: jakx/kmachine_extras.cpp"
Cohesion: 0.11
Nodes (35): alloc_vagdir_names(), bool_to_symbol(), callback_fetch_external_highscores(), callback_fetch_external_race_times(), callback_fetch_external_speedrun_times(), init_autosplit_struct(), pc_fetch_external_highscores(), pc_fetch_external_race_times() (+27 more)

### Community 273 - "game/system: GameController"
Cohesion: 0.08
Nodes (14): GameController, m_device_handle, m_device_name, m_guid, m_has_led, m_has_pressure_sensitive_buttons, m_has_rumble, m_has_trigger_rumble (+6 more)

### Community 274 - "goalc/build_level: CollideFragment"
Cohesion: 0.06
Nodes (34): CollideBucket, count, index, CollideFragment, axis_scale, bbox_max_corner, bbox_max_corner_i, bbox_min_corner (+26 more)

### Community 275 - "goalc/build_level: EntityActor"
Cohesion: 0.07
Nodes (23): ActorGroup, actors, id, slot, add_actor_groups_from_json(), add_actors_from_json(), EntityActor, aid (+15 more)

### Community 276 - "goalc/build_level: EntityActor"
Cohesion: 0.07
Nodes (23): ActorGroup, actors, id, slot, add_actor_groups_from_json(), add_actors_from_json(), EntityActor, aid (+15 more)

### Community 277 - "common/goos: Node"
Cohesion: 0.09
Nodes (31): append_node_to_string(), break_list(), compute_extra_offset(), insert_required_breaks(), Kind, ATOM, IMPROPER_LIST, INVALID (+23 more)

### Community 278 - "common/type_system: Field"
Cohesion: 0.05
Nodes (15): Field, m_alignment, m_array, m_array_size, m_comment, m_decomp_as_ts, m_dynamic, m_field_score (+7 more)

### Community 280 - "game/graphics: Draw"
Cohesion: 0.05
Nodes (35): Draw, fade, first_bone, first_index, flags, hash, index_count, light_idx (+27 more)

### Community 281 - "goalc/build_level: CollideFragment"
Cohesion: 0.06
Nodes (33): CollideBucket, count, index, CollideFragment, axis_scale, bbox_max_corner, bbox_max_corner_i, bbox_min_corner (+25 more)

### Community 282 - "goalc/compiler: SymbolInfo"
Cohesion: 0.05
Nodes (36): DefinitionLocation, char_idx, file_path, line_idx, SymbolInfo, m_args, m_def_form, m_def_location (+28 more)

### Community 283 - "test: CodeTester"
Cohesion: 0.08
Nodes (19): CodeTester, code_buffer, code_buffer_capacity, code_buffer_size, m_gen, m_info, execute_equals(), execute_equals_4arg() (+11 more)

### Community 284 - "lsp/protocol: CompletionItem"
Cohesion: 0.07
Nodes (33): get_completions(), CompletionItem, additionalTextEdits, commitCharacters, detail, documentation, filterText, insertText (+25 more)

### Community 285 - "goalc/build_actor: NodeWithTransform"
Cohesion: 0.10
Nodes (25): find_single_skin(), flatten_nodes_from_all_scenes(), NodeWithTransform, node_idx, w_T_node, convert_joint(), convert_joints(), extract_skeleton() (+17 more)

### Community 286 - "decompiler/level_extractor: BspHeader"
Cohesion: 0.05
Nodes (35): AdgifShaderArray, adgifs, BspHeader, actors, adgifs, ambients, bsphere, collide_hash (+27 more)

### Community 287 - "docs/progress-notes: Merc renderer (VU1 merc "
Cohesion: 0.08
Nodes (40): BLERC notes, BLERC (merc blend shape face animation), blerc-init, merc-blend-shape, setup-blerc-chains, blerc-execute flow, Determining which fragments can be blerc'd, merc-blend-ctrl per fragment, PC blerc draw lists (normal, non-blerc, blerc), bones.gc skinning matrix notes, bones.gc skinning matrix computation (+32 more)

### Community 288 - "goalc/build_actor: CompressedAnim"
Cohesion: 0.06
Nodes (31): CompressedAnim, fixed, framerate, frames, joint_metadata, master_art_group_index, master_art_group_name, matrix_animated (+23 more)

### Community 289 - "goalc/compiler: Label"
Cohesion: 0.06
Nodes (27): Condition, a, b, is_float, is_signed, kind, ConditionKind, EQUAL (+19 more)

### Community 290 - "goalc/emitter: VEX3"
Cohesion: 0.06
Nodes (22): Instruction, instr, InstructionImpl, VEX2, L, prefix, R, reg_id (+14 more)

### Community 291 - "test/goalc: TEST_F()"
Cohesion: 0.05
Nodes (6): ControlStatementTests, compiler, runner, runtime_thread, testCategory, TEST_F()

### Community 292 - "decompiler/level_extractor: extract_level.cpp"
Cohesion: 0.10
Nodes (16): print_memory_usage(), SimpleThreadGroup, m_func, m_joined, m_threads, add_all_textures_from_level(), confirm_textures_identical(), extract_all_levels() (+8 more)

### Community 293 - "common/custom_data: MemoryUsageCategory"
Cohesion: 0.05
Nodes (39): MemoryUsageCategory, BLERC, COLLISION, HFRAG_CORNERS, HFRAG_INDEX, HFRAG_TIME_OF_DAY, HFRAG_VERTS, MERC_DRAW (+31 more)

### Community 294 - "common/dma: Kind"
Cohesion: 0.05
Nodes (37): Kind, BASE, CALL, CNT, DIRECT, DIRECTHL, END, FLUSH (+29 more)

### Community 295 - "common/goos: SourceText"
Cohesion: 0.10
Nodes (9): SourceText, m_offset_by_line, m_text, TextDb, m_fragments, m_map, TextRef, frag (+1 more)

### Community 296 - "common/serialization: GameSubtitleDefinitionFi"
Cohesion: 0.07
Nodes (34): GameSubtitleDefinitionFile, language_id, lines_base_path, lines_path, meta_base_path, meta_path, text_version, convert_v1_to_v2() (+26 more)

### Community 297 - "game/graphics: GraphicsData"
Cohesion: 0.06
Nodes (29): FrameLimiter, m_timer, GraphicsData, debug_gui, dma_copier, dma_cv, dma_mutex, engine_timer (+21 more)

### Community 298 - "goalc/compiler: Kind"
Cohesion: 0.05
Nodes (39): Kind, ADD, DIV, FTOI, ITOF, MAX, MIN, MUL (+31 more)

### Community 299 - "decompiler/IR2: AtomicOpTypeAnalysis.cpp"
Cohesion: 0.16
Nodes (23): AsmBranchOp::propagate_types_internal(), AsmOp::propagate_types_internal(), AtomicOp::propagate_types(), AtomicOp::reg_type_info_as_string(), BranchOp::propagate_types_internal(), CallOp::propagate_types_internal(), ConditionalMoveFalseOp::propagate_types_internal(), FunctionEndOp::propagate_types_internal() (+15 more)

### Community 300 - "decompiler/IR2: ConditionElement"
Cohesion: 0.05
Nodes (11): ConditionElement, m_consumed, m_flipped, m_kind, m_src, LoadSourceElement, m_addr, m_kind (+3 more)

### Community 301 - "game/graphics: PcTextureAnimCodesJak2"
Cohesion: 0.05
Nodes (38): anim_code_to_info(), FixedAnimInfoJak2, anim_array_idx, code, name, FixedAnimInfoJak3, anim_array_idx, code (+30 more)

### Community 302 - "game/overlord: VagStrListNode"
Cohesion: 0.05
Nodes (36): List, buffer, elt_count, maybe_any_in_use, name, next, sema, unk2_init0 (+28 more)

### Community 303 - "lsp/protocol: LSPSpec::from_json()"
Cohesion: 0.08
Nodes (31): Location, m_range, m_uri, LSPSpec::from_json(), LSPSpec::Range::Range(), LSPSpec::to_json(), MarkupContent, m_kind (+23 more)

### Community 304 - "test: TEST()"
Cohesion: 0.07
Nodes (6): get_floats(), put_floats(), run_vec(), TEST(), VecMem, buf

### Community 305 - "common/formatter: FormFormattingConfig"
Cohesion: 0.08
Nodes (34): FormFormattingConfig, combine_first_two_lines, config_set, default_index_config, determine_column_widths_for_list_elements, elide_top_level_newline, force_inline, hang_forms (+26 more)

### Community 306 - "game/graphics: Merc2.cpp"
Cohesion: 0.13
Nodes (6): fnv64(), blerc_avx(), Merc2::Merc2(), Merc2::ShaderMercMat::to_string(), set_uniform(), tag_is_nothing_next()

### Community 307 - "game/kernel: FocusStatus"
Cohesion: 0.05
Nodes (37): FocusStatus, Arrestable, Board, Carry, Dangerous, Dark, Dead, Disable (+29 more)

### Community 308 - "game/kernel: FocusStatus"
Cohesion: 0.05
Nodes (37): FocusStatus, Arrestable, Board, Carry, Dangerous, Dark, Dead, Disable (+29 more)

### Community 309 - "decompiler/Disasm: DecodeType"
Cohesion: 0.06
Nodes (33): DecodeStep, decode, field, is_src, DecodeType, BC, BRANCH_TARGET, COP0 (+25 more)

### Community 310 - "decompiler/gui: decompiler_gui.py"
Cohesion: 0.08
Nodes (9): DgoFile, FileMap, get_jak_path(), get_monospaced_font(), load_obj_map_file(), ObjectFileBrowser, ObjectFileView, ObjFile (+1 more)

### Community 311 - "decompiler/IR2: SetVarElement"
Cohesion: 0.06
Nodes (11): SetVarElement, m_dst, m_is_sequence_point, m_src, m_src_type, m_var_info, WithDmaBufferAddBucketElement, m_body (+3 more)

### Community 312 - "game/mips2c: Cache"
Cohesion: 0.05
Nodes (29): Cache, adgif_shader_texture_simple, clip_polygon_against_negative_hyperplane, clip_polygon_against_positive_hyperplane, draw_large_polygon, fake_scratchpad_data, lookup_texture_by_id_fast, math_camera (+21 more)

### Community 313 - "game/overlord: CBaseFile"
Cohesion: 0.06
Nodes (17): CBaseFile, m_Buffer, m_FileDef, m_FileKind, m_LengthPages, m_nNumPages, m_PageOffset, m_ProcessDataSemaphore (+9 more)

### Community 314 - "game/overlord: ISO_DGOCommand"
Cohesion: 0.06
Nodes (32): ISO_DGOCommand, acked_cancel_id, buffer1, buffer2, buffer_toggle, buffer_top, bytes_processed, dgo_header (+24 more)

### Community 315 - "game/overlord: ISO_DGOCommand"
Cohesion: 0.06
Nodes (32): ISO_DGOCommand, acked_cancel_id, buffer1, buffer2, buffer_toggle, buffer_top, bytes_processed, dgo_header (+24 more)

### Community 316 - "game/sound: GrainType"
Cohesion: 0.06
Nodes (36): GrainType, ADD_PB, ADD_REGISTER, BRANCH, CONTROL_NULL, COPY_REGISTER, DEC_REGISTER, GOTO_MARKER (+28 more)

### Community 317 - "game/system: IOP"
Cohesion: 0.07
Nodes (19): IOP, allocations, cv, ee_main_mem, IOP::IOP(), iop_mutex, iop_run_cv, kernel (+11 more)

### Community 318 - "goalc/build_level: Material"
Cohesion: 0.06
Nodes (36): Material, CARPET, CRMETAL, CRWOOD, DEEPSNOW, DIRT, DMAKER, FOREST (+28 more)

### Community 319 - "goalc/debugger: DebugServer"
Cohesion: 0.07
Nodes (22): Compiler, DebugServer, m_client_sockets, m_compiler, m_compiler_mutex, m_event_mutex, m_event_queue, m_file_breakpoints (+14 more)

### Community 320 - "lsp/protocol: Diagnostic"
Cohesion: 0.08
Nodes (28): CodeDescription, m_href, Diagnostic, m_code, m_codeDescription, m_message, m_range, m_relatedInformation (+20 more)

### Community 321 - "common/dma: GsPrim"
Cohesion: 0.06
Nodes (21): GsPrim, data, Kind, LINE, LINE_STRIP, POINT, PRIM_7, SPRITE (+13 more)

### Community 322 - "common/type_system: StateHandler"
Cohesion: 0.10
Nodes (24): func_to_state_type(), get_state_handler_arg_names(), get_state_handler_type(), get_state_type_from_enter_and_code(), get_state_type_from_func(), handler_keyword_to_kind(), handler_kind_to_name(), handler_name_to_kind() (+16 more)

### Community 323 - "decompiler/Disasm: Gpr"
Cohesion: 0.06
Nodes (35): Gpr, A0, A1, A2, A3, AT, FP, GP (+27 more)

### Community 324 - "game/mips2c: Gpr"
Cohesion: 0.06
Nodes (35): ShaderLibrary::ShaderLibrary(), Gpr, a0, a1, a2, a3, at, fp (+27 more)

### Community 325 - "game/overlord: jakx/rpc_interface.h"
Cohesion: 0.07
Nodes (33): DgoFno, CANCEL, LOAD, LOAD_NEXT, LoadToEEFno, LOAD_FILE, Rpc_Loader_Bank_Cmd, bank_name (+25 more)

### Community 326 - "goalc/debugger: SourceStackFrame"
Cohesion: 0.07
Nodes (31): Disassembly, failed, text, LiveVariable, in_register, is_parameter, name, reg (+23 more)

### Community 327 - "scripts/modding: package_texture_pack.py"
Cohesion: 0.11
Nodes (16): compare_directories(), hash_file(), build_texture_pack_from_source(), compute_sha256(), derive_release_download_url(), detect_active_game(), detect_author(), detect_current_branch() (+8 more)

### Community 328 - "scripts/modding: create_mod_repo.py"
Cohesion: 0.13
Nodes (21): adjust_migrated(), adjust_new(), ask(), ask_new_mod(), catalog_mods(), close_worktree(), git(), is_ancestor() (+13 more)

### Community 329 - "decompiler/IR2: AtomicOpForm.cpp"
Cohesion: 0.17
Nodes (23): get_as_reg_offset(), AsmBranchOp::get_as_form(), AsmOp::get_as_form(), BranchOp::get_as_form(), BranchOp::get_condition_as_form(), CallOp::get_as_form(), ConditionalMoveFalseOp::get_as_form(), FunctionEndOp::get_as_form() (+15 more)

### Community 330 - "decompiler/Disasm: Cop0"
Cohesion: 0.06
Nodes (34): Cop0, BADPADDR, BADVADDR, CAUSE, COMPARE, CONFIG, CONTEXT, COP0_STATUS (+26 more)

### Community 331 - "decompiler/IR2: SimpleExpressionElement"
Cohesion: 0.10
Nodes (4): SimpleExpressionElement, m_expr, m_my_idx, SimpleExpressionElement::update_from_stack()

### Community 332 - "decompiler/IR2: Maps"
Cohesion: 0.07
Nodes (21): GenericOpMatcher, m_condition_kind, m_fixed_kind, m_func_matcher, m_kind, m_sub_matchers, LetEntryMatcher, m_kind (+13 more)

### Community 334 - "game/kernel: common/kmemcard.cpp"
Cohesion: 0.14
Nodes (26): file_is_present(), MC_check_result(), mc_checksum(), MC_createfile(), MC_format(), mc_get_filename(), mc_get_filename_no_dir(), MC_get_status() (+18 more)

### Community 335 - "game/kernel: mc_slot_info"
Cohesion: 0.07
Nodes (30): mc_file_info, data, present, mc_slot_info, files, formatted, handle, initted (+22 more)

### Community 336 - "game/kernel: FocusStatus"
Cohesion: 0.06
Nodes (34): FocusStatus, Arrestable, Board, Carry, Dangerous, Dark, Dead, Disable (+26 more)

### Community 337 - "game/mips2c: jak2_functions/merc_blen"
Cohesion: 0.07
Nodes (28): blerc_c(), BlercBlock, header, output, BlercBlockHeader, lump_dst, lump_qwc, overlap (+20 more)

### Community 338 - "goalc/make: Tool"
Cohesion: 0.09
Nodes (21): compile_dir_tpages(), compile_game_count(), Tool, m_name, AppendSbkTool, m_reader, BuildActor2Tool, m_reader (+13 more)

### Community 339 - "goalc/emitter: .set_op2()"
Cohesion: 0.08
Nodes (30): call_r64(), ja_imm(), jae_imm(), jb_imm(), jbe_imm(), je_imm(), jg_imm(), jge_imm() (+22 more)

### Community 340 - "tools/memory_dump_tool: memory_dump_tool/main.cp"
Cohesion: 0.20
Nodes (18): build_symbol_map(), build_type_map(), find_basics(), follow_references_to_find_pointers(), in_memory(), inspect_basics(), inspect_process_self(), inspect_symbols() (+10 more)

### Community 341 - "scripts/ci: lint-characters.py"
Cohesion: 0.08
Nodes (24): Lint workflow (fast source checks on every push), Forbidden assert() check (C++ engine), Autoglottonyms left untranslated check, Allowed characters in translation files check, og:preserve-this marker removal check (goal_src), Trailing whitespace check (goal_src), util/Assert.cpp assertion support, serialization subsystem (text and subtitles v1/v2) (+16 more)

### Community 342 - "test/goalc: TEST_F()"
Cohesion: 0.06
Nodes (8): SharedCompiler, compiler, runner, runtime_thread, TEST_F(), VariableTests, shared_compiler, testCategory

### Community 343 - "common/texture: process_tpage()"
Cohesion: 0.10
Nodes (21): CPSM, PSMCT16, PSMCT32, PSM, PSMCT16, PSMCT32, PSMT4, PSMT8 (+13 more)

### Community 344 - "common/util: Hunk"
Cohesion: 0.10
Nodes (20): CalculateOptimalEdits(), CreateUnifiedDiff(), diff_strings(), EditType, kAdd, kMatch, kRemove, kReplace (+12 more)

### Community 345 - "decompiler/IR2: VariableNames"
Cohesion: 0.09
Nodes (19): promote_register_class(), try_lookup_read(), try_lookup_write(), mode, hash, RegId, id, reg (+11 more)

### Community 346 - "decompiler/IR2: AsmOp"
Cohesion: 0.06
Nodes (12): AsmOp, m_dst, m_instr, m_src, LoadVarOp, m_dst, m_kind, m_size (+4 more)

### Community 347 - "decompiler/VuDisasm: VuDisassembler"
Cohesion: 0.07
Nodes (23): OpInfo, decode, known, name, VuDecodeStep, atom, field, VuDisassembler (+15 more)

### Community 348 - "docs/img: Mod detail page (hero ba"
Cohesion: 0.09
Nodes (33): Add mod step 1: Launcher Mods settings tab (screenshot), Add (Ajouter) button (annotation 2), Mod source URL field, Mods settings tab (General, Versions, Decompiler, Mods, Backgrounds), OpenGOAL Launcher (v2.11.1, Outils v0.3.6), Settings gear button (annotation 1), Add mod step 2: Launcher Mods catalog page (screenshot), Mod filters (text search, game selector, sort by Popularity) (+25 more)

### Community 349 - "game/mips2c: FprName"
Cohesion: 0.06
Nodes (33): FprName, f0, f1, f10, f11, f12, f13, f14 (+25 more)

### Community 350 - "goalc/build_sbk: GrainData"
Cohesion: 0.06
Nodes (33): GrainData, adpcm, adsr1, adsr2, center_fine, center_note, ctrl, delay (+25 more)

### Community 351 - "goalc/emitter: X86_REG"
Cohesion: 0.06
Nodes (33): X86_REG, R10, R11, R12, R13, R14, R15, R8 (+25 more)

### Community 352 - "common/custom_data: Vertex"
Cohesion: 0.06
Nodes (26): CollisionMesh, vertices, hash, Vertex, a, b, cluster_idx, color_index (+18 more)

### Community 353 - "common/util: string_util.cpp"
Cohesion: 0.13
Nodes (28): contains(), current_isotimestamp(), current_local_timestamp(), current_local_timestamp_no_colons(), diff(), ends_with(), join(), line_count() (+20 more)

### Community 354 - "decompiler/extractor: ExtractorErrorCode"
Cohesion: 0.09
Nodes (25): calculate_extraction_hash(), ExtractorErrorCode, COMPILATION_BAD_PROJECT_PATH, DECOMPILATION_GENERIC_ERROR, EXTRACTION_INVALID_ISO_PATH, EXTRACTION_ISO_UNEXPECTED_SIZE, INVALID_CLI_INPUT, INVALID_CLI_INPUT_MISSING_FOLDER (+17 more)

### Community 355 - "decompiler/analysis: variable_naming.cpp"
Cohesion: 0.15
Nodes (14): arg_reg_idx(), is_arg_reg(), is_possible_coloring_move(), is_saved_reg(), reg_to_string(), SSA::Block::print(), SSA::Ins::print(), SSA::Phi::print() (+6 more)

### Community 356 - "decompiler/level_extractor: extract_collide_frags()"
Cohesion: 0.12
Nodes (18): build_all_frags_list(), CollideListItem, inst, mesh, unpacked, debug_dump_to_obj(), extract_collide_frags(), extract_pats() (+10 more)

### Community 357 - "game/graphics: GLDisplay"
Cohesion: 0.07
Nodes (24): DisplayState, pending_size_change, requested_size_height, requested_size_width, window_pos_x, window_pos_y, window_scale_x, window_scale_y (+16 more)

### Community 358 - "game/graphics: TexturePool.cpp"
Cohesion: 0.14
Nodes (3): goal_string(), TexturePool::TexturePool(), upload_to_gpu()

### Community 359 - "goalc/compiler: algorithm"
Cohesion: 0.10
Nodes (7): CodeGenerator, m_debug_info, m_fe, m_gen, DebugInfo, record_local_variables(), TypeSystem

### Community 360 - "common/type_system: StructureType"
Cohesion: 0.06
Nodes (10): StructureType, m_allow_misalign, m_always_stack_singleton, m_dynamic, m_fields, m_idx_of_first_unique_field, m_offset, m_overriden_fields (+2 more)

### Community 361 - "common/util: read_iso_file.cpp"
Cohesion: 0.10
Nodes (19): add_from_dir(), Entry, children, is_dir, name, offset_in_file, size, find_files_in_iso() (+11 more)

### Community 362 - "decompiler/Function: ControlFlowGraph"
Cohesion: 0.12
Nodes (9): ControlFlowGraph, m_blocks, m_entry, m_exit, m_has_break, m_node_pool, m_uid, for_each_top_level_vtx() (+1 more)

### Community 363 - "decompiler/VuDisasm: VuDisassembler.cpp"
Cohesion: 0.15
Nodes (20): bc_to_part(), get_label_name(), has_branch_delay(), is_nop(), lower_op(), mask_to_string(), upper_bc(), upper_dest_mask() (+12 more)

### Community 364 - "game/mips2c: Cache"
Cohesion: 0.07
Nodes (28): Cache, camera_pos, debug_draw_settings, fake_scratchpad_data, flush_cache, gsf_buffer, math_camera, shadow_add_double_edges (+20 more)

### Community 365 - "game/mips2c: Cache"
Cohesion: 0.06
Nodes (28): Cache, display, dma_bucket_insert_tag, fake_scratchpad_data, generic_envmap_proc, generic_light_proc, generic_merc_death, generic_merc_execute_asm (+20 more)

### Community 366 - "game/overlord: jak3/rpc_interface.h"
Cohesion: 0.09
Nodes (29): LoadToEEFno, LOAD_FILE, Rpc_Loader_Bank_Cmd, bank_name, pad, Rpc_Loader_Get_Irx_Version, ee_addr, major (+21 more)

### Community 367 - "game/overlord: SoundIOPInfo"
Cohesion: 0.06
Nodes (31): SoundIOPInfo, chinfo, dirtycd, diskspeed, dupseg, frame, freemem, freemem2 (+23 more)

### Community 368 - "game/overlord: SoundIOPInfo"
Cohesion: 0.06
Nodes (31): SoundIOPInfo, chinfo, dirtycd, diskspeed, dupseg, frame, freemem, freemem2 (+23 more)

### Community 369 - "goalc/build_level: collide_pack.cpp"
Cohesion: 0.12
Nodes (21): dedup_frag_mesh(), IndexedFaces, faces, vertices_float, vertices_u16, IndexFace, pat_idx, vertex_indices (+13 more)

### Community 370 - "goalc/emitter: s64"
Cohesion: 0.15
Nodes (28): lea_reg_plus_off(), lea_reg_plus_off32(), lea_reg_plus_off8(), load128_simd128_gpr64_s32(), load128_simd128_gpr64_s8(), load128_simd128_reg_offset(), load16s_pcRel_s32(), load16u_pcRel_s32() (+20 more)

### Community 371 - "goalc/emitter: .set_disp()"
Cohesion: 0.10
Nodes (20): load128_simd128_gpr64(), load64_gpr64_plus_s32(), load_goal_simd128(), loadvf_gpr64_plus_gpr64(), loadvf_gpr64_plus_gpr64_plus_s32(), loadvf_gpr64_plus_gpr64_plus_s8(), loadvf_rip_plus_s32(), store128_gpr64_simd128() (+12 more)

### Community 372 - "scripts/gsrc: utils.py"
Cohesion: 0.11
Nodes (14): AllTypesUpdateBlock, get_all_blocks(), update_all_blocks(), update_alltypes_named_blocks(), has_form_ended(), is_line_start_of_form(), LinterRule, LintMatch (+6 more)

### Community 373 - "goalc/build_actor: jak1/build_level.cpp"
Cohesion: 0.11
Nodes (10): MercEyeAnimBlock, frames, max_frame, MercEyeAnimFrame, blink, iris_scale, lid_scale, pupil_scale (+2 more)

### Community 374 - "decompiler/analysis: SSA"
Cohesion: 0.08
Nodes (18): Block, ins, phis, Ins, dst, is_arg_coloring_move, is_dead_set, is_gpr_fpr_coloring_move (+10 more)

### Community 375 - "decompiler/Disasm: Disasm/Register.cpp"
Cohesion: 0.16
Nodes (9): cop0_to_charp(), fpr_to_charp(), gpr_to_charp(), hash, Register, id, special_to_charp(), vf_to_charp() (+1 more)

### Community 376 - "decompiler/Function: CfgVtx"
Cohesion: 0.07
Nodes (17): CfgVtx, end_branch, needs_label, next, parent, pred, prev, succ_branch (+9 more)

### Community 377 - "decompiler/IR2: LabelInfo"
Cohesion: 0.09
Nodes (14): DecompiledDataElement::DecompiledDataElement(), LabelDB, LabelDB::LabelDB(), m_info, m_labels_by_name, m_labels_by_offset_into_seg, LabelInfo, array_size (+6 more)

### Community 378 - "decompiler/IR2: VectorFloatLoadStoreElem"
Cohesion: 0.07
Nodes (11): RegClass, VF, RLetElement, body, sorted_regs, VectorFloatLoadStoreElement, m_addr_type, m_is_load (+3 more)

### Community 379 - "game/external: discord.cpp"
Cohesion: 0.11
Nodes (15): FOCUS_TEST, get_base_level_name(), get_full_level_name(), get_time_of_day(), handleDiscordJoinRequest(), handleDiscordReady(), indoors(), init_discord_rpc() (+7 more)

### Community 380 - "game/graphics: MercDebugStats"
Cohesion: 0.07
Nodes (27): DrawDebug, mode, num_tris, EffectDebug, draws, envmap, envmap_mode, MercDebugStats (+19 more)

### Community 381 - "game/kernel: VehicleType"
Cohesion: 0.07
Nodes (30): VehicleType, evan_test_bike, h_bike_a, h_bike_b, h_bike_c, h_bike_d, h_car_a, h_car_b (+22 more)

### Community 382 - "game/kernel: VehicleType"
Cohesion: 0.07
Nodes (30): VehicleType, evan_test_bike, h_bike_a, h_bike_b, h_bike_c, h_bike_d, h_car_a, h_car_b (+22 more)

### Community 383 - "game/mips2c: Cache"
Cohesion: 0.07
Nodes (27): Cache, camera_pos, debug_draw_settings, fake_scratchpad_data, flush_cache, gsf_buffer, shadow_add_double_edges, shadow_add_double_tris (+19 more)

### Community 384 - "game/overlord: SoundIopInfo"
Cohesion: 0.07
Nodes (27): SoundIopInfo, chinfo, dirtycd, diskspeed, dupseg, frame, freemem, freemem2 (+19 more)

### Community 385 - "goalc/compiler: SymbolInfoMap"
Cohesion: 0.20
Nodes (4): SymbolInfoMap, m_file_symbol_index, m_symbol_map, m_textdb

### Community 386 - "goalc/debugger: InstructionPointerInfo"
Cohesion: 0.09
Nodes (17): BacktraceFrame, rip_info, rsp_at_rip, InstructionPointerInfo, func_debug, function_name, function_offset, goal_rip (+9 more)

### Community 387 - "scripts/modding: switch_mod.py"
Cohesion: 0.13
Nodes (17): git(), kb_is_submodule(), kb_unpushed_work(), list_targets(), main(), mod_branch(), owner(), ref_exists() (+9 more)

### Community 388 - "goalc/build_actor: animation_processing.cpp"
Cohesion: 0.12
Nodes (14): extract_vec(), n, can_use_small_trans(), compress_animation(), compress_frame_to_matrix(), compress_quat(), compress_scale(), compress_trans() (+6 more)

### Community 389 - "common/type_system: deftype.cpp"
Cohesion: 0.26
Nodes (21): car, for_each_in_list(), add_bitfield(), add_field(), BitFieldTypeDefResult, flags, generate_runtime_type, cdr() (+13 more)

### Community 390 - "common/serialization: subtitles_v2.cpp"
Cohesion: 0.12
Nodes (21): from_json(), SubtitleCutsceneLineMetadataV1, clear, frame_start, offscreen, speaker, SubtitleFileV1, cutscenes (+13 more)

### Community 391 - "decompiler/analysis: analyze_ir2_register_usa"
Cohesion: 0.10
Nodes (19): analyze_ir2_register_usage(), in_set(), PerBlock, defs, input, output, use, PerOp (+11 more)

### Community 392 - "decompiler/Function: FunctionName"
Cohesion: 0.09
Nodes (17): FunctionKind, GLOBAL, METHOD, NV_STATE, TOP_LEVEL_INIT, UNIDENTIFIED, V_STATE, FunctionName (+9 more)

### Community 393 - "decompiler/level_extractor: PrototypeBucketTie"
Cohesion: 0.07
Nodes (28): PrototypeArrayTie, allocated_length, content_type, data, length, PrototypeBucketTie, base_qw, collide_frag (+20 more)

### Community 394 - "decompiler/ObjectFile: LetRewriteStats"
Cohesion: 0.07
Nodes (26): LetRewriteStats, abs, abs2, attack_info, call_parent_state_handler, case_no_else, case_with_else, countdown (+18 more)

### Community 395 - "decompiler/util: Kind"
Cohesion: 0.07
Nodes (29): Kind, DYNAMIC_METHOD_ACCESS, ENTER_STATE_FUNCTION, FALSE_AS_NULL, FIND_PARENT_METHOD_FUNCTION, FORMAT_STRING, GET_ART_BY_NAME_METHOD, INTEGER_CONSTANT (+21 more)

### Community 396 - "game/mips2c: Cache"
Cohesion: 0.07
Nodes (26): Cache, active, add_to_sprite_aux_list, atan, cos, level, math_camera, new_sound_id (+18 more)

### Community 398 - "goalc/compiler: IntegerMathKind"
Cohesion: 0.08
Nodes (25): IntegerMathKind, ADD_64, AND_64, IDIV_32, IMOD_32, IMUL_32, IMUL_64, NOT_64 (+17 more)

### Community 399 - "test: TEST()"
Cohesion: 0.12
Nodes (12): Array, Boolean, check_first_float(), check_first_integer(), check_first_string(), check_first_symbol(), first_array_matches(), first_char_matches() (+4 more)

### Community 400 - "common/util: font_utils_korean.cpp"
Cohesion: 0.12
Nodes (18): from_json(), codepoint_to_utf8(), compose_jamo(), compose_jamo_characters(), font_util_korean::compose_korean_containing_text(), font_util_korean::game_encode_korean_syllable(), glyph_hex_string_to_int(), is_jamo_character() (+10 more)

### Community 401 - "game/system: IopThread"
Cohesion: 0.08
Nodes (20): EventFlag, multiple_waiters_allowed, value, wait_list, EventFlagWaiter, mode, pattern, thread (+12 more)

### Community 402 - "custom_assets/blender_plugins: gltf2_blender_extract.py"
Cohesion: 0.11
Nodes (12): __apply_mat_to_all(), __calc_morph_tangents(), extract_primitives(), __get_bitangent_signs(), __get_bone_data(), __get_colors(), __get_normals(), __get_positions() (+4 more)

### Community 403 - "decompiler/util: StackSpillMap"
Cohesion: 0.09
Nodes (16): build_spill_map(), StackInstrInfo, is_load, is_signed, kind, size, StackSpillMap::add_access(), StackSpillMap::finalize() (+8 more)

### Community 404 - "decompiler/IR2: OpenGOALAsm"
Cohesion: 0.07
Nodes (22): Function, funcTemplate, modifiers, InstructionModifiers, ACC_THIRD_SRC_ARG, BROADCAST, DEST_MASK, FSF (+14 more)

### Community 405 - "game/overlord: Jak 2 Overlord Port Note"
Cohesion: 0.11
Nodes (28): Per-game Overlord implementations, Jak 2 Overlord Port Notes, dma changes (DmaVagCmd, instant DMA, no semaphore), fakeiso (made up ISO layer), iso.c (ISO threads and DGO state machine), iso_api.c (EE-facing ISO/VAG API), iso_cd.c (CD callbacks), iso_queue.c (buffers and message queue) (+20 more)

### Community 406 - "game/graphics: LevelData"
Cohesion: 0.08
Nodes (23): LevelData, collide_vertices, frames_since_last_used, hfrag_indices, hfrag_vertices, level, load_id, merc_indices (+15 more)

### Community 407 - "game/graphics: OceanMid_PS2.cpp"
Cohesion: 0.16
Nodes (16): clip(), erleng(), fcand(), fcor(), OceanMid::run_call107_vu2c(), OceanMid::run_call107_vu2c_jak2(), OceanMid::run_call275_vu2c(), OceanMid::run_call275_vu2c_jak2() (+8 more)

### Community 408 - "game/graphics: SpriteFrameData"
Cohesion: 0.07
Nodes (28): SpriteFrameData, adgif_giftag, basis_x, basis_y, bonus, clipped_giftag, deg_to_rad, fog_max (+20 more)

### Community 409 - "game/graphics: SpriteFrameDataJak1"
Cohesion: 0.07
Nodes (27): SpriteFrameDataJak1, adgif_giftag, basis_x, basis_y, bonus, clipped_giftag, deg_to_rad, fog_max (+19 more)

### Community 410 - "game/mips2c: Cache"
Cohesion: 0.08
Nodes (25): Cache, camera_pos, fake_scratchpad_data, flush_cache, gsf_buffer, math_camera, shadow_add_double_edges, shadow_add_double_tris (+17 more)

### Community 411 - "game/mips2c: Cache"
Cohesion: 0.08
Nodes (23): Cache, bone_calculation_list, display, fake_scratchpad_data, foreground, foreground_generic_merc, foreground_generic_merc_add_fragments, foreground_generic_merc_death (+15 more)

### Community 412 - "game/mips2c: Cache"
Cohesion: 0.08
Nodes (23): Cache, bone_calculation_list, display, fake_scratchpad_data, foreground, foreground_generic_merc, foreground_generic_merc_add_fragments, foreground_generic_merc_death (+15 more)

### Community 413 - "game/mips2c: Cache"
Cohesion: 0.08
Nodes (23): Cache, bone_calculation_list, display, fake_scratchpad_data, foreground, foreground_generic_merc, foreground_generic_merc_add_fragments, foreground_generic_merc_death (+15 more)

### Community 414 - "game/system: KeyboardDevice"
Cohesion: 0.09
Nodes (10): InputDevice, m_loaded, m_settings, ActiveKeyboardAction, binding, revert_action, sdl_keycode, KeyboardDevice (+2 more)

### Community 415 - "game/system: IOP_Kernel"
Cohesion: 0.10
Nodes (17): IOP_Kernel, _currentThread, event_flags, IOP_Kernel::IOP_Kernel(), kernel_thread, m_start_time, mainThreadSleep, mbxs (+9 more)

### Community 416 - "lsp/protocol: ProgressNotificationPayl"
Cohesion: 0.13
Nodes (23): LSPSpec::from_json(), LSPSpec::to_json(), ProgressNotificationPayload, beginValue, endValue, reportValue, token, WorkDoneProgressBegin (+15 more)

### Community 417 - "decompiler/analysis: M2C_Block"
Cohesion: 0.12
Nodes (22): block_requires_label(), handle_branch_reg2(), handle_likely_branch_bc(), handle_non_likely_branch_bc(), handle_unknown(), link_branch(), link_fall_through(), link_fall_through_likely() (+14 more)

### Community 418 - "decompiler/analysis: SymbolMapBuilder"
Cohesion: 0.12
Nodes (14): Function, get_loaded_or_stored_symbol_name(), ObjectFileData, ObjectSymbolList, object_file_name, symbols, SymbolInfo, is_type (+6 more)

### Community 419 - "decompiler/IR2: RegAccessSet"
Cohesion: 0.08
Nodes (9): BreakElement, dead_code, lid, return_code, StoreInPairElement, m_is_car, m_my_idx, m_pair (+1 more)

### Community 420 - "decompiler/ObjectFile: LinkedWord"
Cohesion: 0.11
Nodes (14): Kind, EMPTY_PTR, HI_PTR, LO_PTR, PLAIN_DATA, PTR, SYM_OFFSET, SYM_PTR (+6 more)

### Community 421 - "game/kernel: codegen.h"
Cohesion: 0.10
Nodes (8): emit_arm64_c_stub(), emit_arm64_mov64(), emit_return_stub(), emit_zero_stub(), flush_icache(), LinkedFunctionTable, m_executes, TEST()

### Community 422 - "common/type_system: FieldReverseLookupOutput"
Cohesion: 0.08
Nodes (20): FieldReverseLookupOutput, addr_of, result_type, success, tokens, total_score, get_type_of_type(), Kind (+12 more)

### Community 423 - "scripts/modding: sync_global_catalog.py"
Cohesion: 0.12
Nodes (13): collect_mods_from_mod_repos(), discover_mod_repos(), fetch_json(), fetch_paged(), generate_global_catalog(), get_default_repo(), get_token(), latest_release_catalog() (+5 more)

### Community 424 - "decompiler/IR2: ArrayFieldAccess"
Cohesion: 0.08
Nodes (12): ArrayFieldAccess, m_constant_offset, m_deref_tokens, m_expected_stride, m_flipped, m_source, StoreArrayAccess, m_base_var (+4 more)

### Community 425 - "decompiler/ObjectFile: ObjectFileData"
Cohesion: 0.08
Nodes (23): for_each_obj_in_dgo(), ObjectFileData, base_name_from_chunk, data, dgo_names, full_output, has_multiple_versions, linked_data (+15 more)

### Community 426 - "game/graphics: Constants"
Cohesion: 0.08
Nodes (22): Constants, constants, constants2, drw_adgif, drw_fan, drw_strip_0, drw_strip_1, drw_texture (+14 more)

### Community 427 - "game/mips2c: Cache"
Cohesion: 0.08
Nodes (23): Cache, add_to_sprite_aux_list, atan, cos, level, math_camera, new_sound_id, particle_adgif (+15 more)

### Community 428 - "game/system: DisplayMode"
Cohesion: 0.08
Nodes (23): DisplayMode, display_name, orientation, refresh_rate, screen_height, screen_width, sdl_display_id, sdl_pixel_format (+15 more)

### Community 429 - "goalc/build_level: add_actors_from_json()"
Cohesion: 0.18
Nodes (13): enum_from_json(), get_enum_or_int(), get_enum_val(), movie_pos_from_json(), parse_enum(), res_from_json_array(), vector_from_json(), vector_vol_from_json() (+5 more)

### Community 430 - "goalc/listener: MemoryMapEntry"
Cohesion: 0.13
Nodes (12): LoadEntry, load_string, segment_sizes, segments, MemoryMap, m_entries, MemoryMapEntry, empty (+4 more)

### Community 431 - "scripts/ai: sys"
Cohesion: 0.13
Nodes (9): git(), main(), update(), is_link(), main(), make_link(), relink(), remove_link() (+1 more)

### Community 433 - "decompiler/Function: Warnings.h"
Cohesion: 0.12
Nodes (16): DecompWarnings, m_warnings, unique_warnings, error(), error_and_throw(), info(), Kind, ERR (+8 more)

### Community 434 - "docs/progress-notes: ETIE (environment-mapped"
Cohesion: 0.09
Nodes (25): TIE Instances BVH and Visibility Bit Strings, TIE VU1 Initialization Block, TIE Per-Instance Data Replication Loop (L2), Jak 1 TIE VU1 Microprogram, DMA Buckets (326 in Jak 2) and Bucket Stitching, draw-inline-array-instance-tie (about 1400 lines of asm), draw-inline-array-prototype-tie-asm, ETIE (environment-mapped TIE) Renderer (+17 more)

### Community 435 - "lsp/protocol: TypeHierarchyItem"
Cohesion: 0.12
Nodes (17): SymbolTag, Deprecated, LSPSpec::from_json(), LSPSpec::to_json(), TypeHierarchyItem, detail, kind, name (+9 more)

### Community 436 - "game/graphics: ProgressRenderer"
Cohesion: 0.09
Nodes (11): ProgressRenderer, kMinimapFbp, kMinimapHeight, kMinimapVramAddr, kMinimapWidth, kScreenFbp, m_current_fbp, m_fb_ctxt (+3 more)

### Community 437 - "game/mips2c: generic_tie.cpp"
Cohesion: 0.19
Nodes (21): Cache, fake_scratchpad_data, execute(), lq_buffer(), sq_buffer(), vcallms_104(), vcallms_114(), vcallms_122() (+13 more)

### Community 438 - "game/mips2c: Cache"
Cohesion: 0.08
Nodes (25): Cache, display, dma_bucket_insert_tag, fake_scratchpad_data, generic_envmap_proc, generic_light_proc, generic_merc_death, generic_merc_execute_asm (+17 more)

### Community 439 - "game/mips2c: Cache"
Cohesion: 0.08
Nodes (25): Cache, display, dma_bucket_insert_tag, fake_scratchpad_data, generic_envmap_proc, generic_light_proc, generic_merc_death, generic_merc_execute_asm (+17 more)

### Community 440 - "game/mips2c: Cache"
Cohesion: 0.08
Nodes (22): Cache, add_to_sprite_aux_list, atan, cos, part_id_table, particle_adgif, particle_adgif_cache, particle_setup_adgif (+14 more)

### Community 441 - "game/overlord: Jak1SoundCommand"
Cohesion: 0.08
Nodes (25): Jak1SoundCommand, CONTINUE_GROUP, CONTINUE_SOUND, GET_IRX_VERSION, LIST_SOUNDS, LOAD_BANK, LOAD_MUSIC, MIRROR_MODE (+17 more)

### Community 442 - "game/overlord: SoundCommand"
Cohesion: 0.08
Nodes (25): SoundCommand, CANCEL_DGO, CONTINUE_GROUP, CONTINUE_SOUND, GET_IRX_VERSION, LIST_SOUNDS, LOAD_BANK, LOAD_MUSIC (+17 more)

### Community 443 - "goalc/build_level: collide_bvh.cpp"
Cohesion: 0.17
Nodes (20): bsphere_recursive(), build_collide_tree(), CNode, bsphere, child_nodes, faces, collect_vertices(), CollideTree (+12 more)

### Community 444 - "goalc/emitter: Rt()"
Cohesion: 0.16
Nodes (25): load16s_gpr64_gpr64_plus_gpr64(), load16s_gpr64_gpr64_plus_gpr64_plus_s8(), load16u_gpr64_gpr64_plus_gpr64(), load16u_gpr64_gpr64_plus_gpr64_plus_s8(), load32s_gpr64_gpr64_plus_gpr64(), load32s_gpr64_gpr64_plus_gpr64_plus_s8(), load32u_gpr64_gpr64_plus_gpr64(), load32u_gpr64_gpr64_plus_gpr64_plus_s8() (+17 more)

### Community 445 - "lsp/protocol: CompletionItemKind"
Cohesion: 0.08
Nodes (25): CompletionItemKind, Class, Color, Constant, Constructor, Enum, EnumMember, Event (+17 more)

### Community 446 - "common/util: os.cpp"
Cohesion: 0.11
Nodes (15): __cpuidex(), CpuInfo, brand, has_avx, has_avx2, has_neon, initialized, model (+7 more)

### Community 447 - "decompiler/ObjectFile: Stats"
Cohesion: 0.08
Nodes (23): Stats, code_bytes, data_bytes, decoded_ops, function_count, n_fp_reg_use, n_fp_reg_use_resolved, total_code_bytes (+15 more)

### Community 448 - "game/graphics: SpriteHud2DPacket"
Cohesion: 0.09
Nodes (17): SpriteHud2DPacket, adgif_giftag, color, sprite_giftag, st0, st1, st2, st3 (+9 more)

### Community 449 - "game/graphics: GpuTexture"
Cohesion: 0.11
Nodes (15): Element, present, val, GpuTexture, gpu_textures, h, is_common, is_placeholder (+7 more)

### Community 450 - "game/kernel: MasterConfig"
Cohesion: 0.08
Nodes (21): kboot_init_globals_common(), MasterConfig, aspect, disable_game, disable_sound, inactive_timeout, jak2_only_unused, language (+13 more)

### Community 451 - "game/kernel: MouseInfo"
Cohesion: 0.09
Nodes (20): KeybdInfo, active, kdata, keys, valid, MouseInfo, active, button0 (+12 more)

### Community 452 - "game/mips2c: MercBucketInfo"
Cohesion: 0.09
Nodes (19): Cache, fake_scratchpad_data, math_camera, merc_bucket_info, merc_global_stats, exec_mpg(), execute(), MercBucketInfo (+11 more)

### Community 453 - "game/mips2c: Cache"
Cohesion: 0.08
Nodes (21): Cache, add_to_sprite_aux_list, cos, level, new_sound_id, particle_adgif, particle_adgif_cache, particle_setup_adgif (+13 more)

### Community 454 - "game/overlord: SoundCommand"
Cohesion: 0.08
Nodes (24): SoundCommand, CANCEL_DGO, CONTINUE_GROUP, CONTINUE_SOUND, GET_IRX_VERSION, LIST_SOUNDS, LOAD_BANK, LOAD_MUSIC (+16 more)

### Community 455 - "goalc/build_actor: BuildActorParams"
Cohesion: 0.10
Nodes (15): BuildActorParams, framerate, gen_collide_mesh, joint_channel, lod_dist, master_ag_map, master_art_group, texture_bucket (+7 more)

### Community 456 - "goalc/compiler: CompilerSettings"
Cohesion: 0.09
Nodes (15): CompilerSettings, check_for_requires, debug_print_ir, debug_print_regalloc, disable_math_const_prop, emit_move_after_return, m_settings, SettingKind (+7 more)

### Community 457 - "goalc/debugger: .describe_value_bits()"
Cohesion: 0.15
Nodes (9): element_stride(), format_enum_value(), format_symbol_name(), GprName, group, label, name, role (+1 more)

### Community 458 - "goalc/debugger: DebugServer.cpp"
Cohesion: 0.25
Nodes (3): float_special_types(), format_unit_number(), int_special_types()

### Community 459 - "goalc/regalloc: RACache"
Cohesion: 0.08
Nodes (23): RACache, control_flow, current_stack_slot, failed_alloc, iregs, live_per_instruction, liveout_per_instr, reusable_full_width_spill_slots (+15 more)

### Community 461 - "test: TEST()"
Cohesion: 0.09
Nodes (3): private_assert_failed(), crc_reference(), TEST()

### Community 462 - "goalc/build_sbk: build_sbk.cpp"
Cohesion: 0.20
Nodes (17): append_sbk_from_dir(), create_sbk_from_dir(), encode_spu_adpcm(), extract_quoted(), extract_wav_ref(), filter_sounds_by_name(), grain_type_from_name(), kv_array4() (+9 more)

### Community 463 - "common/dma: FixedChunkDmaCopier"
Cohesion: 0.10
Nodes (18): DmaData, data, start_offset, stats, FixedChunkDmaCopier, chunk_size, m_chunk_count, m_chunk_mask (+10 more)

### Community 464 - "common/goos: ObjectType"
Cohesion: 0.10
Nodes (18): ObjectType, ARRAY, CHAR, EMPTY_LIST, ENVIRONMENT, FLOAT, INTEGER, INVALID (+10 more)

### Community 465 - "decompiler/data: StrFileReader.cpp"
Cohesion: 0.19
Nodes (10): extract_name(), find_string_in_data(), FullName, chunk_idx, name, get_string_of_max_length(), StrFileReader, m_chunks (+2 more)

### Community 466 - "docs/progress-notes: Control flow quirks of t"
Cohesion: 0.10
Nodes (23): Macro pattern matching (planned), Statement to S-Expression map tree (planned), Variable declaration and scoping (planned), Jak 1 decompilation notes (GOAL operations and idioms), Function call arguments evaluated in order, Begin-like forms flush immediately (docstring compiled as string constant), Bitwise opcodes (or, and, nor, xor), Common idioms (ash, abs, min, max) (+15 more)

### Community 467 - "game/graphics: TextureUploadHandler"
Cohesion: 0.11
Nodes (9): TextureUpload, mode, page, TextureUploadHandler, m_direct, m_fake_uploads, m_texture_animator, m_upload_count (+1 more)

### Community 468 - "game/graphics: OceanTextureConstants"
Cohesion: 0.09
Nodes (18): MipMap, vao, vtx_buffer, OceanTextureConstants, buffers, cam_nrm, constants, dests (+10 more)

### Community 469 - "game/sce: libpad.cpp"
Cohesion: 0.13
Nodes (19): CPadGetData(), CPadInfo, PadMode, Controller, DualShock, DualShock2, Joystick, NamcoGun (+11 more)

### Community 470 - "game/system: DS5EffectsState_t"
Cohesion: 0.09
Nodes (22): DS5EffectsState_t, rgucLeftTriggerEffect, rgucRightTriggerEffect, rgucUnknown1, rgucUnknown2, ucAudioEnableBits, ucAudioMuteBits, ucEnableBits1 (+14 more)

### Community 471 - "game/system: EEInputEvent"
Cohesion: 0.09
Nodes (19): EEInputEvent, param1, param2, param3, param4, param5, type, EEInputEventType (+11 more)

### Community 472 - "goalc/compiler: Atoms.cpp"
Cohesion: 0.17
Nodes (11): Compiler::compile(), Compiler::compile_char(), Compiler::compile_float(), Compiler::compile_get_sym_obj(), Compiler::compile_get_symbol_value(), Compiler::compile_integer(), Compiler::compile_no_const_prop(), Compiler::compile_pair() (+3 more)

### Community 473 - "goalc/compiler: ConstantPropagation.cpp"
Cohesion: 0.18
Nodes (11): code_size(), Compiler::const_prop_begin(), Compiler::const_prop_gscond(), Compiler::constant_propagation_dispatch(), Compiler::get_constant_float_or_variable(), Compiler::get_constant_integer_or_error(), Compiler::get_constant_integer_or_variable(), Compiler::try_constant_propagation() (+3 more)

### Community 474 - "lsp/protocol: DocumentSymbol"
Cohesion: 0.13
Nodes (15): document_symbols(), ir_symbols(), og_symbols(), DocumentSymbol, m_children, m_detail, m_kind, m_name (+7 more)

### Community 475 - "lsp/protocol: SymbolKind"
Cohesion: 0.09
Nodes (23): SymbolKind, Class, Constant, Constructor, Enum, EnumMember, Event, Field (+15 more)

### Community 477 - "decompiler/analysis: get_defstate_entries()"
Cohesion: 0.22
Nodes (11): get_defstate_entries(), get_state_info(), is_nonvirtual_state(), rewrite_nonvirtual_defstate(), rewrite_nonvirtual_defstate_with_inherit(), rewrite_virtual_defstate_with_nonvirtual_inherit(), run_defstate(), strip_cast() (+3 more)

### Community 478 - "decompiler/IR2: AshElement"
Cohesion: 0.09
Nodes (9): AbsElement, consumed, source, AshElement, clobber, consumed, is_signed, shift_amount (+1 more)

### Community 479 - "goalc/retarget_anim: retarget_anim.cpp"
Cohesion: 0.21
Nodes (17): add_accessor(), add_channel(), compact_model(), constant_curve(), Curve, flat_values, is_quat, decompose_matrix() (+9 more)

### Community 480 - "decompiler/VuDisasm: .decode()"
Cohesion: 0.18
Nodes (3): VuInstructionAtom, m_kind, m_value

### Community 481 - "docs/modding: GitHub Actions Workflows"
Cohesion: 0.16
Nodes (21): GitHub Actions Workflows Guide, Workflow access control (owner-only actor checks), Workflow architecture (upstream to master to master-dev to mod repositories), build.yml, lint.yml, mod-suggestion-triage.yml, Mother repository guard (endsWith /jak-project), og:preserve-this removal lint (lint-gsrc-removals.py) (+13 more)

### Community 482 - "game/graphics: BufferBlitState"
Cohesion: 0.09
Nodes (21): BufferBlitState, dbp, dbw, dpsm, dsax, dsay, expect, height (+13 more)

### Community 483 - "game/kernel: SpeedrunPracticeEntry"
Cohesion: 0.10
Nodes (20): SpeedrunPracticeEntry, completed_task, continue_point_name, end_task, end_zone_v1, end_zone_v2, features, flags (+12 more)

### Community 484 - "game/kernel: SpeedrunPracticeEntry"
Cohesion: 0.10
Nodes (20): SpeedrunPracticeEntry, completed_task, continue_point_name, end_task, end_zone_v1, end_zone_v2, features, flags (+12 more)

### Community 485 - "game/mips2c: jak1_functions/generic_m"
Cohesion: 0.26
Nodes (17): execute(), lq_buffer(), lq_xyzw(), sq_buffer(), sq_xyzw(), vcallms_280(), vcallms_303(), vcallms_311() (+9 more)

### Community 486 - "game/overlord: CDvdDriver"
Cohesion: 0.09
Nodes (20): CDvdDriver, current_thread_priority, disk_type, event_flag, fifo_access_sema, fifo_entry_sema, initialized, kNumFileCacheEntries (+12 more)

### Community 487 - "goalc/build_level: Event"
Cohesion: 0.09
Nodes (22): Event, BURN, BURNUP, DEADLY, DEADLYUP, DRAG, ENDLESSFALL, FRY (+14 more)

### Community 488 - "goalc/regalloc: LiveInfo"
Cohesion: 0.10
Nodes (10): LiveInfo, assignment, best_hint, has_constraint, indices_of_alive, is_alive, max, min (+2 more)

### Community 489 - "lsp/protocol: DidChangeTextDocumentPar"
Cohesion: 0.15
Nodes (18): DidChangeTextDocumentParams, m_contentChanges, m_textDocument, DidCloseTextDocumentParams, m_textDocument, DidOpenTextDocumentParams, m_textDocument, LSPSpec::from_json() (+10 more)

### Community 490 - "common/util: T"
Cohesion: 0.22
Nodes (10): Node, children, value, Trie<T>::find_longest_prefix(), Trie<T>::get_all_nodes(), Trie<T>::insert(), Trie<T>::lookup(), Trie<T>::lookup_prefix() (+2 more)

### Community 491 - "misc: test-script.py"
Cohesion: 0.14
Nodes (10): analyze(), classify(), Color, compare_exact(), Function, normalize_registers(), Operation, parse_file() (+2 more)

### Community 492 - "decompiler/analysis: final_output.cpp"
Cohesion: 0.21
Nodes (12): add_indent(), append_body_to_function_definition(), careful_function_to_string(), final_defun_out(), final_output_defstate_anonymous_behavior(), final_output_lambda(), fix_docstring_indent(), FunctionDefSpecials (+4 more)

### Community 493 - "docs/modding: Taskfile.yml developer c"
Cohesion: 0.14
Nodes (20): Decompiler README, Install the tools and extract the game, Junctions sharing iso_data, decompiler_out and out game folders, task modding-switch (single-folder switching), Switching mods needs extract plus forced compile (make-group iso :force), One git worktree per mod, Task Commands and Modding Scripts Reference, Asset ripping tasks (rip-textures, rip-levels, rip-collision, rip-audio) (+12 more)

### Community 494 - "docs/modding: How the Repository Works"
Cohesion: 0.16
Nodes (20): Commit, push and keep up with master-dev, Create the mod repository (task modding-new-mod), Record verified discoveries in the knowledge base, How the Repository Works, Archived mod branches as archive/<branch> tags, Knowledge base submodule (opengoal-modding-kb at .agents/skills), Mod repository (<game>-mod-<slug>), Mother repository (jak-project, master and master-dev) (+12 more)

### Community 495 - "docs/setup: Visual Studio Setup Guid"
Cohesion: 0.12
Nodes (21): Visual Studio Setup Guide, VS 2026 CMake endless-build bug, VS 2022 IntelliSense issue with clang, Windows Release (clang) build configuration, VSCode Setup Guide, clangd extension for VSCode, Zed Setup Guide, Zed built-in clangd C++ support (+13 more)

### Community 496 - "game/graphics: SpriteGlowOutput"
Cohesion: 0.11
Nodes (15): Sprite3DMatrixData, camera, hvdf_offset, SpriteGlowOutput, adgif, first_clear_pos, flare_draw_color, flare_xyzw (+7 more)

### Community 497 - "game/kernel: SpeedrunPracticeEntry"
Cohesion: 0.10
Nodes (19): SpeedrunPracticeEntry, completed_task, continue_point_name, end_task, end_zone_v1, end_zone_v2, features, flags (+11 more)

### Community 498 - "game/overlord: jak3/dvd_driver.cpp"
Cohesion: 0.15
Nodes (3): CMsg::CMsg(), CMsgCancelRead::CMsgCancelRead(), DvdThread()

### Community 499 - "game/sce: sceMcTblGetDir"
Cohesion: 0.10
Nodes (17): sceMcStDateTime, day, hour, min, month, sec, unk, year (+9 more)

### Community 500 - "common/util: BinaryWriter"
Cohesion: 0.25
Nodes (9): BinaryWriter, data, build_dgo(), build_name_table(), bw_bytes(), find_fa_offset(), grow_name_table_tail(), wrap_fa() (+1 more)

### Community 501 - "common/util: TrieWithDuplicates"
Cohesion: 0.20
Nodes (6): TrieNode, children, elements, TrieWithDuplicates, root, Compiler::find_symbols_or_object_file_by_prefix()

### Community 502 - "decompiler/Disasm: FieldType"
Cohesion: 0.10
Nodes (20): FieldType, BC, DEST, FD, FS, FS_F, FT, FT_F (+12 more)

### Community 503 - "decompiler/VuDisasm: AtomK"
Cohesion: 0.10
Nodes (20): AtomK, ASSERT_ZERO, BC, BRANCH_TARGET, DST_ACC, DST_MASK, DST_P, DST_Q (+12 more)

### Community 504 - "game/graphics: OceanNear_PS2.cpp"
Cohesion: 0.18
Nodes (9): clip(), eleng(), fcand(), fcor(), OceanNear::run_L15_vu2c(), OceanNear::run_L15_vu2c_jak2(), OceanNear::run_L25_vu2c(), OceanNear::run_L25_vu2c_jak2() (+1 more)

### Community 505 - "game/kernel: DiscordInfo"
Cohesion: 0.10
Nodes (17): AutoSplitterBlock, marker, pointer_to_symbol, DiscordInfo, buzzer_total, cutscene, deaths, flutflut (+9 more)

### Community 506 - "game/mips2c: jak2_functions/generic_m"
Cohesion: 0.27
Nodes (15): execute(), lq_buffer(), lq_xyzw(), sq_buffer(), sq_xyzw(), vcallms_280(), vcallms_303(), vcallms_311() (+7 more)

### Community 507 - "game/mips2c: Cache"
Cohesion: 0.12
Nodes (14): Cache, atan, cos, cos_poly_vec, display, fake_scratchpad_data, ntsc, pal (+6 more)

### Community 508 - "game/mips2c: jak3_functions/generic_m"
Cohesion: 0.27
Nodes (15): execute(), lq_buffer(), lq_xyzw(), sq_buffer(), sq_xyzw(), vcallms_280(), vcallms_303(), vcallms_311() (+7 more)

### Community 509 - "game/mips2c: Cache"
Cohesion: 0.12
Nodes (14): Cache, atan, cos, cos_poly_vec, display, fake_scratchpad_data, ntsc, pal (+6 more)

### Community 510 - "game/mips2c: Cache"
Cohesion: 0.12
Nodes (14): Cache, atan, cos, cos_poly_vec, display, fake_scratchpad_data, ntsc, pal (+6 more)

### Community 511 - "game/overlord: Jak 3 Overlord TODO"
Cohesion: 0.14
Nodes (19): ssound.c (sound state, volume, pan), Jak 3 Overlord TODO, Alternate (dolby) playback modes hit outside Freedom HQ, Changing file size, goal_src update, Pan calculation wrong: now uses a 989snd table, UpdateVolume, Jak X Overlord TODO (+11 more)

### Community 512 - "goalc/build_level: TieOutput"
Cohesion: 0.11
Nodes (17): CollideOutput, faces, Output, collide, tfrag, tie, TfragOutput, color_palette (+9 more)

### Community 513 - "goalc/compiler: Macro.cpp"
Cohesion: 0.21
Nodes (11): Compiler::compile_defconstant(), Compiler::compile_defglobalconstant(), Compiler::compile_define_constant(), Compiler::compile_goos_macro(), Compiler::compile_gscond(), Compiler::compile_macro_expand(), Compiler::compile_mlet(), Compiler::compile_quote() (+3 more)

### Community 514 - "goalc/compiler: ConstantValue"
Cohesion: 0.15
Nodes (6): ConstantValue, m_size, m_value, U128, hi, lo

### Community 515 - "goalc/debugger: disassemble_x86_function"
Cohesion: 0.12
Nodes (11): Breakpoint, goal_addr, id, old_data, ContinueInfo, addr_breakpoint, is_addr_breakpiont, subtract_1 (+3 more)

### Community 516 - "test: test_emitter_arm64.cpp"
Cohesion: 0.15
Nodes (7): id, arm64_call_for_regalloc_test(), as_float(), as_u32(), for_each_gpr_except(), for_each_register_except(), for_each_register_except_stack_and_scratch()

### Community 517 - "decompiler/level_extractor: ProgramInfo"
Cohesion: 0.11
Nodes (19): ProgramInfo, adgif_offset_in_gif_buf_qw, extra, gifbufs, kick_addr, misc_x, point_ptr, skip_bp2 (+11 more)

### Community 518 - "decompiler/util: FieldKind"
Cohesion: 0.11
Nodes (19): FieldKind, CPUINFO_FLAGS, DEGREES, DEGREES_PER_SEC, END_FLAG, FLOAT, FLOAT_PER_SEC, FUNCTION (+11 more)

### Community 519 - "decompiler/VuDisasm: VuInstruction"
Cohesion: 0.11
Nodes (12): VuInstruction, bc, dst, first_src_field, fp, iemdt, kind, mask (+4 more)

### Community 520 - "docs/scratch: TIE Format Document"
Cohesion: 0.11
Nodes (19): TIE Clipped W Calculation, TIE Instance Flags (0b01 no DMA, 0b10 generic renderer), TIE Instance Out Data (6 qw: matrix, morph constants, flags/clip/clipped_w, color tags), TIE Origin Matrix 16-bit Compression, TIE Format Document, TIE Total Camera Matrix (origin times shrub matrix), TIE Wind System (64 winds, wind-time, stiffness), Wind Vectors (proxy-prototype-array-tie and *wind-work*) (+11 more)

### Community 521 - "docs/progress-notes: Emerc (environment-mappe"
Cohesion: 0.12
Nodes (19): Emerc Envmap Texture-Coordinate Math (unperspect, transformed normal, eleng, Q), Emerc (environment-mapped merc) Renderer, Emerc Selection Conditions (emerc effect bit, scene-player actor, outside scissor-frame range), Emerc VU1 Low Memory Map (tri-strip giftag, adgif giftag, hvdf, perspective, fog, unperspect), Emerc VU1 Programs (0 per-frame init, 19 effect init, 29 process fragment), Emerc to Merc Backward Compatibility and Distance Fallback, generic-envmap-proc, generic-merc-query (+11 more)

### Community 522 - "game/graphics: SpriteGlowData"
Cohesion: 0.11
Nodes (14): glow_math(), Sprite3::glow_dma_and_draw(), SpriteGlowData, color, dummy, fade_a, fade_b, pos (+6 more)

### Community 523 - "game/graphics: GoalTexture"
Cohesion: 0.11
Nodes (15): GoalTexture, clut_dest, clutpsm, dest, h, masks, mip_shift, name_ptr (+7 more)

### Community 524 - "game/graphics: TexturePool"
Cohesion: 0.12
Nodes (12): TexturePool, m_id_to_name, m_loaded_textures, m_mt4hh_textures, m_mutex, m_name_to_id, m_next_pc_texture_to_allocate, m_placeholder_data (+4 more)

### Community 525 - "game/kernel: McStatusCode"
Cohesion: 0.11
Nodes (19): McStatusCode, BAD_HANDLE, BAD_VERSION, BUSY, FORMAT_FAILED, INTERNAL_ERROR, NEW_GAME, NO_AUTO_SAVE (+11 more)

### Community 526 - "game/kernel: MouseInfo"
Cohesion: 0.11
Nodes (15): MouseInfo, active, button0, cursor, deltax, deltay, id, pad (+7 more)

### Community 527 - "game/mips2c: Cache"
Cohesion: 0.12
Nodes (13): Cache, atan, cos, cos_poly_vec, fake_scratchpad_data, ntsc, pal, ripple_update_waveform_offs (+5 more)

### Community 528 - "game/mips2c: Cache"
Cohesion: 0.12
Nodes (16): Cache, collide_cache, collide_edge_hold_list, collide_edge_work, edge_grabbed, format, matrix, send_event_function (+8 more)

### Community 529 - "game/mips2c: Cache"
Cohesion: 0.12
Nodes (16): Cache, collide_cache, collide_edge_hold_list, collide_edge_work, edge_grabbed, format, matrix, send_event_function (+8 more)

### Community 530 - "goalc/build_sbk: SoundData"
Cohesion: 0.18
Nodes (13): build_sblk(), build_sblk_entries(), build_sblk_entries_v2(), do_append_sbk(), fcc(), SoundData, flags, grains (+5 more)

### Community 531 - ".agents/skills: OpenGOAL Modding Knowled"
Cohesion: 0.17
Nodes (17): custom-actors-levels skill, documentalist skill, REPL workflow document, engine-internals skill, goal-lisp skill, Lisp wiki index.md, opengoal-modding-kb repository (git submodule at .agents/skills), Knowledge-base recording procedure (find, one home, edit in place, cite, push) (+9 more)

### Community 532 - "common/math: geometry.h"
Cohesion: 0.16
Nodes (9): affine_inverse(), bsphere_of_triangle(), inverse(), point_in_bsphere(), ray_sphere_intersect(), RaySphereResult, hit, u (+1 more)

### Community 533 - "common/util: CopyOnWrite"
Cohesion: 0.22
Nodes (5): CopyOnWrite, m_data, ObjectAndCount, m_count, object

### Community 534 - "decompiler/Disasm: Vi"
Cohesion: 0.11
Nodes (18): Vi, CLIPPING, CMSAR0, CMSAR1, COP2_INVALID14, COP2_INVALID3, COP2_INVALID7, COP2_INVALID8 (+10 more)

### Community 535 - "decompiler/ObjectFile: LinkedObjectFile"
Cohesion: 0.11
Nodes (10): LinkedObjectFile, functions_by_seg, label_db, label_per_seg_by_offset, labels, offset_of_data_zone_by_seg, segments, stats (+2 more)

### Community 536 - "docs/img: jak-project/iso_data/jak"
Cohesion: 0.12
Nodes (16): iso_data/jak1 folder listing screenshot, Disc root files (DISK_ID.DIZ, SYSTEM.CNF, Z6TAIL.DUP), Disc data folders (CGO, DGO, DRIVERS, MUS, SBK, STR, TEXT, VAG, VIS), jak-project/iso_data/jak1 extracted disc layout, SCUS_971.24 (PS2 game executable, 518 KB), OpenGOAL logo (colored text version), Yellow-orange emblem replacing the final L-O of the wordmark, OpenGOAL project branding (+8 more)

### Community 537 - "docs/progress-notes: GOAL language changelog "
Cohesion: 0.13
Nodes (18): GOAL language changelog (V0.1 to V1.0), Process behaviors and state support (:behavior, defbehavior, :state), Bitfield types (up to 128-bit), GOAL language V0.1, GOAL language V0.2, GOAL language V0.3, GOAL language V0.4, GOAL language V0.5 (+10 more)

### Community 538 - "game/graphics: Uniforms"
Cohesion: 0.11
Nodes (17): ModBuffers, vao, vertex, Uniforms, decal, fade, fog, fog_color (+9 more)

### Community 539 - "game/kernel: Type"
Cohesion: 0.11
Nodes (16): Type, allocated_size, asize_of_method, copy_method, delete_method, heap_base, inspect_method, length_method (+8 more)

### Community 540 - "game/kernel: Type"
Cohesion: 0.11
Nodes (16): Type, allocated_size, asize_of_method, copy_method, delete_method, heap_base, inspect_method, length_method (+8 more)

### Community 541 - "game/kernel: Type"
Cohesion: 0.11
Nodes (16): Type, allocated_size, asize_of_method, copy_method, delete_method, heap_base, inspect_method, length_method (+8 more)

### Community 542 - "game/kernel: SpeedrunPracticeObjectiv"
Cohesion: 0.11
Nodes (18): SpeedrunPracticeObjective, completed_task, end_task, end_zone, end_zone_init_params, features, flags, index (+10 more)

### Community 543 - "game/kernel: Type"
Cohesion: 0.11
Nodes (16): Type, allocated_size, asize_of_method, copy_method, delete_method, heap_base, inspect_method, length_method (+8 more)

### Community 544 - "game/overlord: SoundIopInfo"
Cohesion: 0.11
Nodes (15): SoundIopInfo, chinfo, dirtycd, diskspeed, dupseg, frame, freemem, freemem2 (+7 more)

### Community 545 - "game/overlord: SoundPlayParams"
Cohesion: 0.11
Nodes (15): Rpc_Player_Set_Fps_Cmd, fps, pad, SoundPlayParams, bend, fo_curve, fo_max, fo_min (+7 more)

### Community 546 - "goalc/compiler: Lambda"
Cohesion: 0.14
Nodes (13): GoalArg, name, type, InlineableFunction, inline_by_default, lambda, type, Lambda (+5 more)

### Community 548 - "lsp/protocol: Hover"
Cohesion: 0.16
Nodes (9): hover(), hover_handler_ir(), is_number(), truncate_docstring(), Hover, m_contents, m_range, LSPSpec::from_json() (+1 more)

### Community 549 - "common/serialization: GameTextDB"
Cohesion: 0.22
Nodes (5): GameTextBank, m_lang_id, m_lines, GameTextDB, m_banks

### Community 550 - "decompiler/analysis: Mips2C_Output"
Cohesion: 0.20
Nodes (13): goal_to_c_function_name(), goal_to_c_name(), handle_daddiu(), handle_generic_store(), handle_lui(), handle_lw(), handle_sw(), Mips2C_Output (+5 more)

### Community 551 - "decompiler: DecompileHacks"
Cohesion: 0.12
Nodes (15): CondWithElseLengthHack, max_length_by_start_block, DecompileHacks, asm_functions_by_name, blocks_ending_in_asm_branch_by_func_name, cond_with_else_len_by_func_name, format_ops_with_dynamic_string_by_func_name, hint_inline_assembly_functions (+7 more)

### Community 552 - "decompiler: string"
Cohesion: 0.12
Nodes (14): LabelConfigInfo, array_size, is_value, type_name, LocalVarOverride, name, type, ObjectPatchInfo (+6 more)

### Community 553 - "decompiler/level_extractor: JointAnimCompressedFixed"
Cohesion: 0.12
Nodes (16): JointAnimCompressedFixed, data, data16, data16_size, data32, data32_size, data64, data64_size (+8 more)

### Community 554 - "docs/modding: How to Create a Mod"
Cohesion: 0.18
Nodes (16): current_mod directory README (Tier 2 mod docs), Naming convention <mod_slug>_readme.md, Recommended structure for mod technical readmes, scripts/modding/sync_common.py branch-sync classification, texture_packs directory for release archives, Tier 2 technical mod documentation, How to Create a Mod, Custom assets (models, sounds, texture replacements, texture packs) (+8 more)

### Community 555 - "docs/progress-notes: calc-animation-from-spr"
Cohesion: 0.15
Nodes (17): Joint Blend Tree Stack Machine (push, push1, float, blend, stack commands), calc-animation-from-spr, channel-upload-info, clear-frame-accumulator, Joint 4-bit Control Modes (16 modes: fixed vs frame trans/quat/scale, big-trans), create-interpolated2-joint-animation-frame, create-interpolated-joint-animation-frame, cspace<-matrix-no-push-joint! (+9 more)

### Community 556 - "game/graphics: CollideMeshRenderer"
Cohesion: 0.15
Nodes (9): CollideMeshRenderer, CollideMeshRenderer::CollideMeshRenderer(), m_colors, m_ubo, m_vao, PatColors, pat_event_colors, pat_material_colors (+1 more)

### Community 557 - "game/kernel: SpeedrunPracticeObjectiv"
Cohesion: 0.12
Nodes (17): SpeedrunPracticeObjective, completed_task, end_task, end_zone, end_zone_init_params, features, flags, index (+9 more)

### Community 558 - "game/overlord: common/sbank.cpp"
Cohesion: 0.15
Nodes (8): AllocateBank(), AllocateBankName(), LookupBank(), LookupSoundIndex(), ReloadBankInfo(), sbank_init_globals(), PrintBankInfo(), ReadBankSoundInfo()

### Community 559 - "game/overlord: DmaQueueEntry"
Cohesion: 0.12
Nodes (13): DmaQueueEntry, command, iop_mem, length, num_isobuffered_chunks, spu_addr, user_data, Info (+5 more)

### Community 560 - "game/overlord: jak3/dvd_driver.h"
Cohesion: 0.13
Nodes (13): BlockParams, CDescriptor, m_File, m_pHead, m_pTail, m_status, m_ThreadID, m_unk0 (+5 more)

### Community 561 - "game/overlord: CPageList"
Cohesion: 0.12
Nodes (16): AllocState, EPLAS_ALLOCATED, EPLAS_FREE, FREE_PENDING, CPageList, m_nAllocState, m_nDmaRefCnt, m_nNumActivePages (+8 more)

### Community 562 - "game/overlord: DmaQueueEntry"
Cohesion: 0.12
Nodes (13): DmaQueueEntry, command, iop_mem, length, num_isobuffered_chunks, spu_addr, user_data, Info (+5 more)

### Community 563 - "game/overlord: CPageList"
Cohesion: 0.12
Nodes (16): AllocState, EPLAS_ALLOCATED, EPLAS_FREE, FREE_PENDING, CPageList, m_nAllocState, m_nDmaRefCnt, m_nNumActivePages (+8 more)

### Community 564 - "game/tools: imgui"
Cohesion: 0.15
Nodes (10): DebugTextFilter, content, type, FiltersMenu, from_json(), to_json(), Type, CONTAINS (+2 more)

### Community 565 - "goalc/build_level: FileInfo"
Cohesion: 0.14
Nodes (10): DataObjectGenerator, FileInfo, file_name, file_type, major_version, maya_file_name, mdb_file_name, minor_version (+2 more)

### Community 566 - "goalc/retarget_anim: SkeletonJoints"
Cohesion: 0.13
Nodes (14): gather_source_anim(), get_skeleton(), Raw, times, value_dim, values, SkeletonJoints, name_to_joint (+6 more)

### Community 567 - "goalc/emitter: CodeTester.cpp"
Cohesion: 0.25
Nodes (7): DisasmLine, address, text, match_pop_gprs(), match_pop_simd(), match_push_gprs(), match_push_simd()

### Community 568 - "common/audio: WaveFileHeader"
Cohesion: 0.12
Nodes (14): WaveFileHeader, aud_format, bits_per_sample, block_align, byte_rate, chunk_id, chunk_size, format (+6 more)

### Community 569 - "common/formatter: OpenGOAL Formatter docum"
Cohesion: 0.17
Nodes (15): OpenGOAL Formatter documentation, AST consolidation and metadata collection, cljfmt, Constant lists and constant pairs (1-space indent), The Hardest Program I've Ever Written (Dart formatter article), flow versus hang formatting, FormatterTree and FormatterNode, game-save.gc nested-let example (about 200 nested lets) (+7 more)

### Community 570 - "common/sqlite: sqlite.h"
Cohesion: 0.17
Nodes (5): SQLite3DatabaseDeleter, sqlite::SQLiteDatabase::open_db(), sqlite::SQLiteDatabase::run_query(), SQLiteDatabase, m_db

### Community 571 - "common/util: BinaryWriter.h"
Cohesion: 0.16
Nodes (11): add(), add_at_ref(), BinaryWriterRef, offset, write_size, DgoDescription, dgo_name, entries (+3 more)

### Community 572 - "common/util: Serializer.h"
Cohesion: 0.23
Nodes (4): from_pod_vector(), from_ptr(), load(), save()

### Community 575 - "docs/progress-notes: Annotated Jak 1 Sprite V"
Cohesion: 0.16
Nodes (16): Clip Test and Zero-Alpha Sprite Reject, Jak 1 Sprite VU1 Program (2D/3D variant), Per-Sprite HVDF Offset Selection (904(vi08)), Jak 1 Sprite VU1 Program (2D screen-space variant), clip_xyz_plus_minus, C++ Port of 2D Sprite VU1 Loop (commented-out), C++ Port of 3D Sprite VU1 Loop (commented-out), Sprite Frame Data (m_frame_data: pfog0, hmge_scale, fog_min/max, min_scale, inv_area, giftags, st_array) (+8 more)

### Community 576 - "docs/progress-notes: Six Sprite Glow Draws"
Cohesion: 0.17
Nodes (16): Sprite xgkick Output Double Buffering, Shadow Output Double Buffer Rotation (mr32 of buffer addresses plus xgkick), Sprite Glow DMA Init (constants, two template copies with init MSCAL, input double buffer, sync), Draw 5: Flare Alpha (repeat-draw-adcmds), Draw 6: Final Glow Draw, Sprite Glow Fade Math (fade = clamp(0,1, p0.z*fade_a + fade_b), rgb *= a), Draw 4: Repeat Draw (texture-filter averaging of alpha), Draw 3: Offscreen Sample (alpha-only copy into temporary texture, GS context 2) (+8 more)

### Community 577 - "game/sound: Synth"
Cohesion: 0.15
Nodes (4): ApplyVolume(), Synth, mVoices, mVolume

### Community 578 - "game/mips2c: Cache"
Cohesion: 0.13
Nodes (13): Cache, already_printed_exeeded_max_cache_tris, cheat_mode, closest_pt_in_triangle, collide_work, debug, fake_scratchpad_data, format (+5 more)

### Community 579 - "game/mips2c: Cache"
Cohesion: 0.12
Nodes (16): Cache, fake_scratchpad_data, generic_envmap_proc, generic_light_proc, generic_prepare_dma_double, generic_prepare_dma_single, gsf_buffer, high_speed_reject (+8 more)

### Community 580 - "game/mips2c: ViName"
Cohesion: 0.12
Nodes (16): ViName, vi00, vi01, vi02, vi03, vi04, vi05, vi06 (+8 more)

### Community 581 - "game/overlord: CPageManager"
Cohesion: 0.20
Nodes (3): alloc_bitmask(), CPageManager, m_CCache

### Community 582 - "game/overlord: CPageManager"
Cohesion: 0.20
Nodes (3): alloc_bitmask(), CPageManager, m_CCache

### Community 583 - "goalc/compiler: IR_FloatMath"
Cohesion: 0.13
Nodes (13): FloatMathKind, ADD_SS, DIV_SS, MAX_SS, MIN_SS, MUL_SS, SQRT_SS, SUB_SS (+5 more)

### Community 584 - ".agents/skills: Jak 2 merc geometry and "
Cohesion: 0.14
Nodes (14): Blender glTF/GLB export workflow, Cross-game model adaptation and retargeting, Cooperative coroutine control, initialize-skeleton (bind model to process), Drive animation: the ja macros, Skeletons and joints (cspace, joint-control), Jak 2 additional verified facts, Live re-skinning a process (+6 more)

### Community 585 - "common: Deci2Header"
Cohesion: 0.15
Nodes (11): Deci2Header, dst, len, proto, rsvd, src, ListenerMessageHeader, deci2_header (+3 more)

### Community 586 - "common/type_system: StructureDefResult"
Cohesion: 0.17
Nodes (11): StructureDefResult, allow_misaligned, always_stack_singleton, flags, generate_runtime_type, pack_me, state_definitions, virtual_state_definitions (+3 more)

### Community 587 - "decompiler/analysis: mips2c.cpp"
Cohesion: 0.23
Nodes (11): Function, handle_generic_op3(), handle_or(), handle_por(), make_vf(), rfp(), rr0(), rra() (+3 more)

### Community 588 - "decompiler/analysis: run_variable_renaming()"
Cohesion: 0.26
Nodes (7): arg_count(), is_128bit(), lca_for_var_types(), make_rc_ssa(), merge_infos(), run_variable_renaming(), update_var_info()

### Community 589 - "decompiler/data: GameCountResult"
Cohesion: 0.15
Nodes (9): CountInfo, buzzer_count, money_count, GameCountResult, info, mystery_data, ObjectFileData, process_game_count() (+1 more)

### Community 590 - "decompiler/Disasm: Disasm/Register.h"
Cohesion: 0.13
Nodes (14): RegisterKind, COP0, FPR, GPR, MAX_KIND, SPECIAL, VF, VI (+6 more)

### Community 591 - "decompiler/Function: string"
Cohesion: 0.13
Nodes (4): EmptyVtx, UntilLoop, body, condition

### Community 592 - "decompiler/Function: Prologue"
Cohesion: 0.13
Nodes (15): Prologue, decoded, epilogue_ok, fp_backed_up, fp_backup_offset, fp_set, fpr_backup_offset, gpr_backup_offset (+7 more)

### Community 593 - "decompiler/level_extractor: JointAnimCompressedFrame"
Cohesion: 0.13
Nodes (14): JointAnimCompressedFrame, data16, data16_size, data32, data32_size, data64, data64_size, mat (+6 more)

### Community 594 - "decompiler/VuDisasm: FieldK"
Cohesion: 0.13
Nodes (15): FieldK, BC, DST_MASK, FD, FS, FSF, FT, FTF (+7 more)

### Community 595 - "docs/img: Zed task spawner palette"
Cohesion: 0.21
Nodes (15): Zed task: Build Project - Debug, Zed task: Build Project - Release, Zed task: Generate CMake - Debug, Zed task: Generate CMake - Release, goalc REPL banner (project path, ISO data path, nREPL 8181), Listener failed to connect (game not running), nREPL listening on port 8181, Zed debug session: REPL - Jak 1 (Windows) (+7 more)

### Community 596 - "game/graphics: Merc2BucketRenderer"
Cohesion: 0.16
Nodes (5): Merc2BucketRenderer, m_debug_stats, m_empty, m_renderer, Merc2BucketRenderer::Merc2BucketRenderer()

### Community 597 - "game/graphics: SpriteGlowConsts"
Cohesion: 0.13
Nodes (15): SpriteGlowConsts, basis_x, basis_y, camera, clamp_max, clamp_min, deg_to_rad, hmge (+7 more)

### Community 598 - "game/graphics: GoalTexturePage"
Cohesion: 0.13
Nodes (13): GoalTexturePage, file_info_ptr, id, length, mip0_size, name_ptr, pad, segment (+5 more)

### Community 599 - "game/kernel: MemoryCardOperation"
Cohesion: 0.13
Nodes (15): MemoryCardOperation, data_ptr, data_ptr2, operation, param, param2, result, retry_count (+7 more)

### Community 600 - "game/mips2c: Cache"
Cohesion: 0.13
Nodes (12): Cache, default_dead_pool, game_info, rand_vu_float_range, spawn_projectile, squid_increment_shield, squid_shot, tan (+4 more)

### Community 601 - "game/mips2c: Cache"
Cohesion: 0.13
Nodes (12): Cache, cheat_mode, closest_pt_in_triangle, collide_puss_work, debug, display_capture_mode, fake_scratchpad_data, format (+4 more)

### Community 602 - "game/mips2c: Cache"
Cohesion: 0.13
Nodes (12): Cache, cheat_mode, closest_pt_in_triangle, collide_puss_work, debug, display_capture_mode, fake_scratchpad_data, format (+4 more)

### Community 603 - "game/overlord: MsgType"
Cohesion: 0.13
Nodes (15): MsgType, ABADBABE, ADEADBEE, DGO_LOAD, LOAD_EE, LOAD_EE_CHUNK, LOAD_IOP, LOAD_SOUNDBANK (+7 more)

### Community 604 - "game/overlord: SoundInfo"
Cohesion: 0.13
Nodes (10): SoundInfo, auto_time, id, name, new_volume, params, sound_handle, VolumePair (+2 more)

### Community 605 - "game/overlord: MsgType"
Cohesion: 0.13
Nodes (15): MsgType, ABADBABE, ADEADBEE, DGO_LOAD, LOAD_EE, LOAD_EE_CHUNK, LOAD_IOP, LOAD_SOUNDBANK (+7 more)

### Community 606 - "game/overlord: SoundInfo"
Cohesion: 0.13
Nodes (10): SoundInfo, auto_time, id, name, new_volume, params, sound_handle, VolumePair (+2 more)

### Community 607 - "game/sound: fifo"
Cohesion: 0.20
Nodes (4): fifo, capacity, read, write

### Community 608 - "goalc/emitter: Immhi()"
Cohesion: 0.29
Nodes (15): load16s_pcRel_s32(), load16u_pcRel_s32(), load8s_pcRel_s32(), load8u_pcRel_s32(), loadvf_rip_plus_s32(), static_addr(), static_load(), static_store() (+7 more)

### Community 609 - "test/goalc: TEST()"
Cohesion: 0.22
Nodes (6): add_common_expected_type_mismatches(), add_jak1_expected_type_mismatches(), add_jak2_expected_type_mismatches(), add_jak3_expected_type_mismatches(), add_jakx_expected_type_mismatches(), TEST()

### Community 610 - "lsp/protocol: FormattingOptions"
Cohesion: 0.19
Nodes (11): DocumentFormattingParams, options, textDocument, FormattingOptions, insertFinalNewLine, insertSpaces, tabSize, trimFinalNewLines (+3 more)

### Community 611 - ".agents/skills: GOAL language traps (sim"
Cohesion: 0.18
Nodes (9): Project file (.gp) registration of new .gc files, GOAL lexical conventions and unit macros, GOAL type system (object, structure, basic, process-drawable), Virtual states and the process state machine, Define a custom actor type (deftype), Define a state (defstate, go vs go-virtual), DGOs and level streaming, Registering a new source file (.gd and game.gp) (+1 more)

### Community 612 - "common/audio: audio_formats.cpp"
Cohesion: 0.26
Nodes (8): break_filter_ties(), decode_adpcm(), encode_block_with_filter(), get_max_bits(), get_shift_error(), saturate(), test_encode_adpcm(), write_wave_file()

### Community 613 - "decompiler/analysis: try_modify_input_types_f"
Cohesion: 0.27
Nodes (4): construct_initial_typestate(), modify_input_types_for_casts(), run_type_analysis_ir2(), try_modify_input_types_for_casts()

### Community 614 - "decompiler/Function: BasicBlock"
Cohesion: 0.14
Nodes (9): BasicBlock, end_word, label_name, pred, start_word, succ_branch, succ_ft, Function (+1 more)

### Community 615 - "decompiler/Function: CfgVtx.h"
Cohesion: 0.15
Nodes (9): alloc(), BasicBlock, Function, GotoEnd, body, unreachable_block, LinkedObjectFile, Object (+1 more)

### Community 616 - "decompiler/level_extractor: common_formats.h"
Cohesion: 0.16
Nodes (9): CompressedMatrixMetadata, is_animated, JointAnimCompressedHDR, control_bits, matrix_bits, num_joints, TextureRemap, new_texid (+1 more)

### Community 617 - "decompiler: ObjectFileDB"
Cohesion: 0.16
Nodes (14): Basic block finding (find_blocks_in_function), Control flow analysis (planned), ObjectFileDB::find_and_write_scripts, ObjectFileDB::find_code, fp-relative static data addressing modes, LinkedObjectFile, LinkedObjectWord and Label, Object file segments (top-level, main, debug), ObjectFileDB (+6 more)

### Community 618 - "decompiler/VuDisasm: Kind"
Cohesion: 0.14
Nodes (12): Kind, ACC, I, IMM, INVALID, LABEL, LOAD_STORE_IMM, P (+4 more)

### Community 619 - "docs/img: Visual Studio build conf"
Cohesion: 0.15
Nodes (14): Visual Studio Build menu screenshot, Build All command (Ctrl+Shift+B), Build gk.exe (bin\gk.exe) target, Install jak command, Rebuild All and Clean All commands, Visual Studio File > Open > CMake menu screenshot, CMake project (repository root CMakeLists), Open > CMake... menu entry (+6 more)

### Community 620 - "docs/modding: mods-menu.gc registry (J"
Cohesion: 0.23
Nodes (12): Lisp wiki (.agents/skills/goal-lisp/wiki), Wire the Mods menu toggle and register new .gc files, Unified In-Game Mods Menu guide, Jak 2 versus Jak 3 popup-menu difference, L3 + SELECT open gesture and menu controls, Migrating a branch from the old debug registry, mods-menu.gc registry (Jak 2 and Jak 3), Naming rules (slug-prefixed config, helpers and builder) (+4 more)

### Community 621 - "docs/progress-notes: foreground-emerc (DMA ge"
Cohesion: 0.15
Nodes (14): Blend Shape (blerc) Per-Fragment DMA Chain, blerc-execute, *blerc-globals*, setup-blerc-chains-for-one-fragment, *default-envmap-shader*, Emerc Extra Transfers vs Merc (unperspect QW, rgba color-fade, 5-QW envmap shader), foreground-draw, foreground-emerc (DMA generation asm) (+6 more)

### Community 622 - "docs/progress-notes: generic-merc-execute-all"
Cohesion: 0.14
Nodes (14): Death Effect (world-space transformed vertices for particles), foreground-generic-merc, foreground-generic-merc-add-fragments, foreground-generic-merc-death, generic-light-proc, generic-merc-death, generic-merc-do-chain, generic-merc-execute-all (+6 more)

### Community 623 - "game/graphics: Shader"
Cohesion: 0.15
Nodes (7): Shader, m_frag_shader, m_is_okay, m_name, m_program, m_vert_shader, shader_folder

### Community 624 - "game/kernel: BindAssignmentInfo"
Cohesion: 0.14
Nodes (12): BindAssignmentInfo, analog_min_range, buttons, device_type, input_idx, port, CommonPCPortFunctionWrappers, intern_from_c (+4 more)

### Community 625 - "game/mips2c: Cache"
Cohesion: 0.15
Nodes (11): Cache, ocean_generate_verts_vector, ocean_vu0_block, ocean_vu0_work, ocean_wave_frames, ocean_work, time_of_day_context, upload_vu0_program (+3 more)

### Community 626 - "game/mips2c: Cache"
Cohesion: 0.14
Nodes (11): Cache, cheat_mode, closest_pt_in_triangle, collide_puss_work, debug, fake_scratchpad_data, format, moving_sphere_sphere_intersect (+3 more)

### Community 627 - "game/mips2c: Cache"
Cohesion: 0.15
Nodes (11): Cache, level, ocean_generate_verts_vector, ocean_vu0_block, ocean_wave_frames, sewerb, time_of_day_context, upload_vu0_program (+3 more)

### Community 628 - "game/mips2c: Cache"
Cohesion: 0.15
Nodes (11): Cache, level, ocean_generate_verts_vector, ocean_vu0_block, ocean_wave_frames, sewerb, time_of_day_context, upload_vu0_program (+3 more)

### Community 629 - "game/mips2c: Cache"
Cohesion: 0.14
Nodes (11): Cache, clip_polygon_against_negative_hyperplane, clip_polygon_against_positive_hyperplane, draw_large_polygon_ocean, fake_scratchpad_data, matrix, ocean_map, sky_work (+3 more)

### Community 630 - "game/overlord: CBaseFileSystem"
Cohesion: 0.14
Nodes (6): CBaseFile, CBaseFileSystem, m_Sema, ISOFileDef, ISOName, VagDirEntry

### Community 631 - "game/overlord: ISO_Hdr"
Cohesion: 0.14
Nodes (14): ISO_Hdr, active_a, active_b, active_c, file_def, m_pBaseFile, mbox_reply, msg_type (+6 more)

### Community 632 - "game/overlord: LogCategory"
Cohesion: 0.14
Nodes (14): LogCategory, DGO, DRIVER, EE_DMA, FILESYSTEM, ISO_QUEUE, NUM_CATETORIES, PAGING (+6 more)

### Community 634 - "game/overlord: SoundPlayParams"
Cohesion: 0.14
Nodes (12): SoundPlayParams, bend, fo_curve, fo_max, fo_min, group, mask, pitch_mod (+4 more)

### Community 635 - "game/overlord: CBaseFileSystem"
Cohesion: 0.14
Nodes (6): CBaseFile, CBaseFileSystem, m_Sema, ISOFileDef, ISOName, VagDirEntry

### Community 636 - "game/overlord: ISO_Hdr"
Cohesion: 0.14
Nodes (14): ISO_Hdr, active_a, active_b, active_c, file_def, m_pBaseFile, mbox_reply, msg_type (+6 more)

### Community 638 - "game/system: sdl_util.cpp"
Cohesion: 0.23
Nodes (10): get_controller_axis_name(), get_controller_button_name(), get_keyboard_button_name(), get_modifier_strings(), get_mouse_button_name(), is_any_event_type(), is_modifier_key(), is_SDL_GUID_zero() (+2 more)

### Community 639 - "game/tools: Entry"
Cohesion: 0.16
Nodes (11): Entry, continue_name, delay_frames, entity_type, execute_code, move_first, move_to, process_name (+3 more)

### Community 640 - "goalc/emitter: InstructionSet"
Cohesion: 0.18
Nodes (5): CodeTester::CodeTester(), InstructionSet, ARM64, X86, ObjectGenerator::ObjectGenerator()

### Community 641 - ".agents/skills: Register an in-game Mods"
Cohesion: 0.19
Nodes (7): Memory and heap architecture (global, level, debug, process), Retail boot vs debug boot, Mod architecture: in-game Mods menu, Register an in-game Mods toggle (mods-menu-register), Simulated PS2 memory block, The three heaps (global, level, debug), Jak 1 Mods toggle not ported (debug-only workaround)

### Community 642 - ".agents/skills: 3-layer mental model (ru"
Cohesion: 0.17
Nodes (11): REPL hot-reload lifecycle ((lt) and (mi)), decompiler and asset extractor, gk game kernel runtime, goalc compiler and REPL, Release packaging and gk exit-code verification, Taskfile command reference, Boot diagnostics and compile/validate loop, Jak 1 compile/validate loop (+3 more)

### Community 643 - "test: TEST()"
Cohesion: 0.21
Nodes (3): Mem, buf, TEST()

### Community 645 - "common/util: image_resize.cpp"
Cohesion: 0.26
Nodes (9): bilinear(), BilinearSample, i0, i1, w0, w1, resize_rgba_image(), sample1() (+1 more)

### Community 646 - "common/util: unicode_util.cpp"
Cohesion: 0.19
Nodes (4): get_env(), utf8_string_to_wide_string(), wide_string_to_utf8_string(), bootstrap_thread_func()

### Community 647 - "decompiler/analysis: FunctionAtomicOps"
Cohesion: 0.15
Nodes (10): BasicBlock, DecompWarnings, Function, FunctionAtomicOps, atomic_op_to_instruction, block_id_to_end_atomic_op, block_id_to_first_atomic_op, instruction_to_atomic_op (+2 more)

### Community 648 - "decompiler/Function: Object"
Cohesion: 0.15
Nodes (4): SequenceVtx, seq, UntilLoop_single, block

### Community 649 - "decompiler/IR2: CondNoElseElement"
Cohesion: 0.15
Nodes (5): CondNoElseElement, already_rewritten, entries, final_destination, used_as_value

### Community 650 - "decompiler/IR2: StackSpillStoreElement"
Cohesion: 0.15
Nodes (6): StackSpillStoreElement, m_access, m_cast_type, m_size, m_stack_offset, m_value

### Community 651 - "decompiler/IR2: UseDefInfo"
Cohesion: 0.15
Nodes (8): AccessRecord, block_id, disabled, op_id, UseDefInfo, defs, ssa_vars, uses

### Community 652 - "decompiler/level_extractor: UncompressedJointAnim"
Cohesion: 0.15
Nodes (10): UncompressedJointAnim, blend_shape_data, framerate, frames, joints, name, UncompressedSingleJointAnim, quat_frames (+2 more)

### Community 653 - "decompiler/level_extractor: extract_actors.cpp"
Cohesion: 0.33
Nodes (6): extract_actors_to_json(), extract_ambients_to_json(), strings_json(), value_json(), vector_json(), vectorm_json()

### Community 654 - "docs/progress-notes: Jak 1 kernel and engine "
Cohesion: 0.24
Nodes (13): Jak 1 kernel and engine code status, Files still marked asm (bounding-box, matrix, transform, quaternion, euler, geometry, vector), dma, dma-buffer and dma-bucket (non-functional sends on PC), gcommon (Done), gkernel (x86-64 changes), gkernel-h (Done), gstate (go from non-main thread), gstring (string->int negative bug) (+5 more)

### Community 655 - "game/graphics: Vertex"
Cohesion: 0.15
Nodes (13): Vertex, a, b, g, r, u, uu, v (+5 more)

### Community 656 - "game/kernel: SpeedrunCustomCategory"
Cohesion: 0.15
Nodes (11): AutoSplitterBlock, marker, pointer_to_symbol, SpeedrunCustomCategory, cheats, completed_task, features, forbidden_features (+3 more)

### Community 657 - "game/kernel: DiscordInfo"
Cohesion: 0.15
Nodes (12): DiscordInfo, current_vehicle, cutscene, death_count, focus_status, gem_count, level, orb_count (+4 more)

### Community 658 - "game/mips2c: Cache"
Cohesion: 0.15
Nodes (10): Cache, add_to_sprite_aux_list, fake_scratchpad_data, quaternion, quaternion_normalize, sp_free_particle, sp_orbiter, sp_relaunch_particle_2d (+2 more)

### Community 659 - "game/mips2c: Cache"
Cohesion: 0.15
Nodes (10): Cache, add_to_sprite_aux_list, fake_scratchpad_data, quaternion, quaternion_normalize, sp_free_particle, sp_orbiter, sp_relaunch_particle_2d (+2 more)

### Community 660 - "game/mips2c: jakx_functions/generic_e"
Cohesion: 0.18
Nodes (10): Cache, fake_scratchpad_data, generic_envmap_proc, generic_no_light_proc, generic_warp_dest_proc, view_get_active_math_camera, viewport_array, execute() (+2 more)

### Community 661 - "game/mips2c: Cache"
Cohesion: 0.15
Nodes (10): Cache, add_to_sprite_aux_list, fake_scratchpad_data, quaternion, quaternion_normalize, sp_free_particle, sp_orbiter, sp_relaunch_particle_2d (+2 more)

### Community 662 - "goalc: compiler library"
Cohesion: 0.24
Nodes (12): sbank.c (sound banks), build_actor tool, build_level tool, build_sbk tool, compiler library, data_compiler (game text, tpage dir, DataObjectGenerator), goalc executable (compiler and REPL), goalc-simple executable (+4 more)

### Community 663 - "game/overlord: BlockParams"
Cohesion: 0.15
Nodes (13): Block, descriptor, next, params, BlockParams, destination, file_def, flag (+5 more)

### Community 664 - "game/overlord: jak3/isocommon.h"
Cohesion: 0.18
Nodes (11): CBaseFile, ISO_LoadSoundbank, bank_info, name, priority, MusicTweaks, MusicTweak, TweakCount (+3 more)

### Community 665 - "game/overlord: CBuffer"
Cohesion: 0.17
Nodes (10): CBuffer, m_eBufferType, m_nDataLength, m_nMaxNumPages, m_nMinNumPages, m_pCurrentData, m_pCurrentPageStart, m_pIsoCmd (+2 more)

### Community 666 - "game/overlord: CCache"
Cohesion: 0.15
Nodes (12): CCache, kAllPagesMask, kNumPageLists, kNumPages, m_nAllocatedMask, m_nNumFreePages, m_nPagelistAllocatedMask, m_paCache (+4 more)

### Community 667 - "game/overlord: CPage"
Cohesion: 0.15
Nodes (12): CPage, input_state, m_nAllocState, m_nDmaRefCount, m_nPageIdx, m_nPageRefCount, m_pNextPage, m_pPageList (+4 more)

### Community 668 - "game/overlord: s32"
Cohesion: 0.18
Nodes (12): Rpc_Loader_Set_Stereo_Mode, mode, Rpc_Player_Play_Cmd, name, pad, params, Rpc_Player_Set_Param_Cmd, auto_from (+4 more)

### Community 669 - "game/overlord: SoundBankInfo"
Cohesion: 0.15
Nodes (11): SoundBankInfo, idx, in_use, loaded, m_name1, m_name2, m_nSpuMemLoc, m_nSpuMemSize (+3 more)

### Community 670 - "game/overlord: BlockParams"
Cohesion: 0.15
Nodes (13): Block, descriptor, next, params, BlockParams, destination, file_def, flag (+5 more)

### Community 671 - "game/overlord: jakx/isocommon.h"
Cohesion: 0.18
Nodes (11): CBaseFile, ISO_LoadSoundbank, bank_info, name, priority, MusicTweaks, MusicTweak, TweakCount (+3 more)

### Community 672 - "game/overlord: CBuffer"
Cohesion: 0.17
Nodes (10): CBuffer, m_eBufferType, m_nDataLength, m_nMaxNumPages, m_nMinNumPages, m_pCurrentData, m_pCurrentPageStart, m_pIsoCmd (+2 more)

### Community 673 - "game/overlord: CCache"
Cohesion: 0.15
Nodes (12): CCache, kAllPagesMask, kNumPageLists, kNumPages, m_nAllocatedMask, m_nNumFreePages, m_nPagelistAllocatedMask, m_paCache (+4 more)

### Community 674 - "game/overlord: CPage"
Cohesion: 0.15
Nodes (12): CPage, input_state, m_nAllocState, m_nDmaRefCount, m_nPageIdx, m_nPageRefCount, m_pNextPage, m_pPageList (+4 more)

### Community 675 - "game/overlord: s32"
Cohesion: 0.18
Nodes (12): Rpc_Loader_Set_Stereo_Mode, mode, Rpc_Player_Play_Cmd, name, pad, params, Rpc_Player_Set_Param_Cmd, auto_from (+4 more)

### Community 676 - "game/overlord: SoundBankInfo"
Cohesion: 0.15
Nodes (11): SoundBankInfo, idx, in_use, loaded, m_name1, m_name2, m_nSpuMemLoc, m_nSpuMemSize (+3 more)

### Community 677 - "goalc/build_sbk: create_sbk()"
Cohesion: 0.21
Nodes (10): append_sbk(), BuildOptions, bank_id, jak1_format, create_sbk(), encode_sounds(), hz_to_note(), note_to_hz() (+2 more)

### Community 678 - ".agents/skills: Documentation pre-flight"
Cohesion: 0.18
Nodes (3): Documentation pre-flight checklist, Information hierarchy (steps, in-file reference, disclosed reference), Progressive disclosure and co-location

### Community 679 - "common/custom_data: tie_normal_transform_v2("
Cohesion: 0.27
Nodes (7): TieTree::unpack(), pack_to_gl_normal(), saturate_for_s10(), tie_normal_transform_v2(), unpack_tie_normal(), vopmsub(), vopmula()

### Community 680 - "common/dma: AdGifData"
Cohesion: 0.17
Nodes (11): AdGifData, alpha_addr, alpha_data, clamp_addr, clamp_data, mip_addr, mip_data, tex0_addr (+3 more)

### Community 681 - "common/goos: string"
Cohesion: 0.23
Nodes (6): FileText, m_desc_name, m_filepath, ProgramString, m_string_name, ReplText

### Community 682 - "common/util: Trie"
Cohesion: 0.17
Nodes (4): Trie, CHAR_SIZE, m_root, m_size

### Community 683 - "decompiler/level_extractor: CompressedAnim"
Cohesion: 0.17
Nodes (12): CompressedAnim, fixed, framerate, frames, joint_metadata, matrix_animated, name, CompressedJointMetadata (+4 more)

### Community 684 - "decompiler/level_extractor: MercSwapInfo"
Cohesion: 0.26
Nodes (4): MercSwapInfo, per_level_custom_mdls, per_level_merc_swaps, swap_list

### Community 686 - "decompiler/types2: types2.h"
Cohesion: 0.17
Nodes (8): for_each_type(), Input, dts, func, function_type, TypePropExtras, needs_rerun, tags_locked

### Community 687 - "decompiler/util: TypeState"
Cohesion: 0.17
Nodes (6): regs_to_gpr_mask(), TypeState, fpr_types, gpr_types, next_state_type, spill_slots

### Community 688 - "docs/progress-notes: Warp Effect (framebuffer"
Cohesion: 0.17
Nodes (12): emerc-vu1-init-buffers, display-frame-finish, fx-copy-buf (chunked framebuffer copy, not yet decompiled), generic-init-buf, generic-translucent, generic-vu1-init-buf-special, generic-vu1-init-buffers, generic-warp-source, generic-warp-envmap-dest, generic-warp-dest (+4 more)

### Community 689 - "docs: game Runtime (C++ Engine"
Cohesion: 0.21
Nodes (12): C Kernel (game/kernel: linker, heaps, symbol table, type system), decompiler (Asset and Code Extraction), Extra Assets (game/assets), game Runtime (C++ Engine and Kernel), goal_src (Game Source Code), goalc (GOAL Compiler and REPL), OVERLORD IOP Driver (game/overlord), OpenGOAL Project Overview (+4 more)

### Community 690 - "game/graphics: VuLights"
Cohesion: 0.17
Nodes (11): VuLights, ambient, color0, color1, color2, direction0, direction1, direction2 (+3 more)

### Community 691 - "game/mips2c: Rng"
Cohesion: 0.30
Nodes (4): pc_rand(), Rng, extra_random_generator, R

### Community 692 - "game/mips2c: Cache"
Cohesion: 0.18
Nodes (9): Cache, clip_polygon_against_negative_hyperplane, clip_polygon_against_positive_hyperplane, draw_boundary_polygon, fake_scratchpad_data, sky_work, view_get_active_math_camera, execute() (+1 more)

### Community 693 - "game/mips2c: Cache"
Cohesion: 0.17
Nodes (9): Cache, clip_polygon_against_negative_hyperplane, clip_polygon_against_positive_hyperplane, draw_large_polygon, fake_scratchpad_data, lookup_texture_by_id_fast, vector_normalize, z_vector (+1 more)

### Community 694 - "game/overlord: Rpc_Player_Base_Cmd"
Cohesion: 0.17
Nodes (11): Rpc_Player_Base_Cmd, command, rsvd1, Rpc_Player_Set_Ear_Trans_Cmd, cam_forward, cam_inverted, cam_left, cam_scale (+3 more)

### Community 695 - "goalc/compiler: Kind"
Cohesion: 0.17
Nodes (12): Kind, CONSTANT, ENUM, FUNCTION, FWD_DECLARED_SYM, GLOBAL_VAR, INVALID, LANGUAGE_BUILTIN (+4 more)

### Community 696 - "lsp/protocol: ColorInformation"
Cohesion: 0.24
Nodes (7): ColorInformation, color, range, DocumentColorParams, textDocument, LSPSpec::from_json(), LSPSpec::to_json()

### Community 697 - "game/sound: flava.h"
Cohesion: 0.22
Nodes (8): FlavaSet, battle_mode, reg, variants, lookup(), Variant, name, value

### Community 699 - "decompiler/Disasm: TEST()"
Cohesion: 0.20
Nodes (6): InstructionParser::InstructionParser(), init_opcode_info(), VDIV, VRSQRT, VSQRT, TEST()

### Community 700 - "decompiler/Function: BlockVtx"
Cohesion: 0.22
Nodes (3): BlockVtx, block_id, is_early_exit_block

### Community 701 - "decompiler/IR2: ConditionalMoveFalseElem"
Cohesion: 0.18
Nodes (5): ConditionalMoveFalseElement, dest, old_value, on_zero, source

### Community 702 - "decompiler/IR2: CondWithElseElement"
Cohesion: 0.18
Nodes (4): CondWithElseElement, already_rewritten, else_ir, entries

### Community 703 - "decompiler/IR2: UntilElement"
Cohesion: 0.18
Nodes (4): UntilElement, body, condition, false_destination

### Community 704 - "decompiler/IR2: WhileElement"
Cohesion: 0.18
Nodes (4): WhileElement, body, cleaned, condition

### Community 705 - "decompiler/level_extractor: ArtData"
Cohesion: 0.20
Nodes (9): ArtData, anims, art_group_name, art_name, joint_group, Joint, bind_pose_T_w, name (+1 more)

### Community 706 - "decompiler/util: DataParser.cpp"
Cohesion: 0.31
Nodes (6): get_until_space(), parse_data(), ParsedData, labels, words, string_to_lines()

### Community 707 - "docs/progress-notes: Generic TIE to ETIE conv"
Cohesion: 0.25
Nodes (11): Generic TIE to ETIE conversion notes, Envmap shader field in prototype-bucket-tie, ETIE (Jak 2 extended TIE) format, Generic TIE renderer data (Jak 1), generic-tie-header type, generic-tie-normal type (int8 x y z), Wrong-normals bug on a few fragments (index_table, normal scale), normal-table-offset as byte offset from header start (+3 more)

### Community 708 - "docs/progress-notes: HFragment (Heightfield T"
Cohesion: 0.25
Nodes (11): HFrag Corner (32x32 grid, 524288 units apart), HFrag C++ Plan (extractor, loader, renderer, GOAL code, debug, textures), HFrag Draw Table (index-linked chains of corners per mode), HFrag Far LOD (spacing 32, poly25, 5 chains, optional scissor), HFragment (Heightfield Terrain) Renderer, Jak 3, HFrag Mid LOD (spacing 16, 9 chains, poly-mid25 and poly-mid), HFrag Near LOD (spacing 8, 17 chains, poly-near, scissoring), pick-level-of-detail (vis bit, sphere cull, guard-band cull) (+3 more)

### Community 709 - "game: runtime static library"
Cohesion: 0.22
Nodes (10): macOS ARM64 build (experimental, unsupported), ARM64 vs x86-64 asm kernel funcs selection, Subtitle editor and filter menu tools, gk executable, HID input system (controllers, keyboard, mouse, display manager), Per-game mips2c function sets, Per-game kernel implementations (jak1/2/3/x), runtime static library (+2 more)

### Community 710 - "game/graphics: Profiler"
Cohesion: 0.20
Nodes (6): BarEntry, duration, rgba, Profiler, m_mode_selector, m_root

### Community 711 - "game/graphics: ScopedProfilerNode"
Cohesion: 0.20
Nodes (3): ScopedProfilerNode, m_global_event, m_node

### Community 712 - "game/graphics: ProfilerNode"
Cohesion: 0.18
Nodes (6): ProfilerNode, m_children, m_finished, m_name, m_stats, m_timer

### Community 713 - "game/graphics: TextureInput"
Cohesion: 0.18
Nodes (9): TextureInput, common, debug_name, debug_page_name, gpu_texture, h, id, src_data (+1 more)

### Community 714 - "game/kernel: DiscordInfo"
Cohesion: 0.18
Nodes (11): DiscordInfo, cutscene, death_count, focus_status, gem_count, level, orb_count, percent_completed (+3 more)

### Community 715 - "game/kernel: SpeedrunCustomCategoryEn"
Cohesion: 0.18
Nodes (10): SpeedrunCustomCategoryEntry, cheats, completed_task, continue_point_name, features, forbidden_features, name, secrets (+2 more)

### Community 716 - "game/mips2c: Cache"
Cohesion: 0.18
Nodes (8): Cache, clip_polygon_against_negative_hyperplane, clip_polygon_against_positive_hyperplane, draw_large_polygon_ocean, fake_scratchpad_data, math_camera, sky_tng_data, execute()

### Community 717 - "game/mips2c: Cache"
Cohesion: 0.18
Nodes (8): Cache, quaternion, sp_frame_time, sp_free_particle, sp_orbiter, sp_relaunch_particle_2d, sp_relaunch_particle_3d, execute()

### Community 718 - "game/mips2c: Cache"
Cohesion: 0.18
Nodes (8): Cache, clear_frame_accumulator, decompress_fixed_data_to_accumulator, decompress_frame_data_pair_to_accumulator, decompress_frame_data_to_accumulator, fake_scratchpad_data, normalize_frame_quaternions, execute()

### Community 719 - "game/mips2c: Cache"
Cohesion: 0.18
Nodes (8): Cache, clear_frame_accumulator, decompress_fixed_data_to_accumulator, decompress_frame_data_pair_to_accumulator, decompress_frame_data_to_accumulator, fake_scratchpad_data, normalize_frame_quaternions, execute()

### Community 720 - "game/overlord: List"
Cohesion: 0.20
Nodes (9): List, buffer, count, name, next, pending_data, sema, unk_flag (+1 more)

### Community 721 - "game/overlord: RPC_Play_Cmd"
Cohesion: 0.18
Nodes (11): RPC_Play_Cmd, address, id, maxlen, names, pad, result, rsvd (+3 more)

### Community 722 - "game/overlord: List"
Cohesion: 0.20
Nodes (9): List, buffer, count, name, next, pending_data, sema, unk_flag (+1 more)

### Community 723 - "game/overlord: RPC_Play_Cmd"
Cohesion: 0.18
Nodes (11): RPC_Play_Cmd, address, id, maxlen, names, pad, result, rsvd (+3 more)

### Community 725 - "game/system: Semaphore"
Cohesion: 0.20
Nodes (10): attribute, fifo, prio, Semaphore, attr, count, initCount, maxCount (+2 more)

### Community 726 - "goalc/compiler: BitFieldVal"
Cohesion: 0.18
Nodes (6): BitFieldVal, m_offset, m_parent, m_sign_extend, m_size, m_use_128

### Community 727 - "goalc/debugger: InstructionInfo"
Cohesion: 0.22
Nodes (9): InstructionInfo, instruction, ir_idx, kind, offset, Kind, EPILOGUE, IR (+1 more)

### Community 728 - "lsp/handlers: initialize()"
Cohesion: 0.15
Nodes (3): initialize(), formatting(), go_to_definition()

### Community 729 - "lsp/state: WorkspaceAllTypesFile"
Cohesion: 0.22
Nodes (5): WorkspaceAllTypesFile, m_dts, m_file_path, m_game_version, m_uri

### Community 730 - "test/goalc: WithGameTests"
Cohesion: 0.18
Nodes (4): get_test_pass_string(), WithGameTests, shared_compiler, testCategory

### Community 731 - ".agents/skills: Lightweight static objec"
Cohesion: 0.20
Nodes (10): build-actor tool, Custom level creation, extract_sbk standalone tool, Grafted entity (Jak 3-to-Jak-1 Jetboard backport), Hand-authoring minimal .glb assets without Blender, Lightweight static objects without skin or Blender, Custom sound banks (SBK audio pipeline), Sound bank architecture (SBK, Overlord, rotating pool) (+2 more)

### Community 732 - "custom_assets/blender_plugins: opengoal.py"
Cohesion: 0.27
Nodes (4): draw_func(), draw_func_ob(), register(), unregister()

### Community 733 - "common/global_profiler: Event profiler (exact ti"
Cohesion: 0.22
Nodes (10): global_profiler subsystem (GlobalProfiler), Event Profiler readme, Capturing a profile (Profiler window, Record, dump to prof.json), Event profiler (exact timeline across frames), Explicit start/stop event functions in gcommon.gc, Fixed-size overwriting event buffer, scoped_prof C++ event (RAII scope), Multi-thread support (EE and graphics threads, ROOT instant events) (+2 more)

### Community 734 - "common/serialization: .write_subtitle_db_to_fi"
Cohesion: 0.29
Nodes (6): dump_language_with_duplicates_from_base(), lookup_locale_code(), dump_bank_lines_v1(), dump_bank_meta_v1(), dump_bank_lines_v2(), dump_bank_meta_v2()

### Community 735 - "common/util: TieFullVertex"
Cohesion: 0.20
Nodes (5): hash, TieFullVertex, color_index, TieFullVertex::hash::operator()(), vertex

### Community 736 - "decompiler/Disasm: AtomKind"
Cohesion: 0.20
Nodes (10): AtomKind, IMM, IMM_SYM, IMM_SYM_VAL_PTR, INVALID, LABEL, REGISTER, VF_FIELD (+2 more)

### Community 737 - "decompiler/IR2: CaseElement"
Cohesion: 0.20
Nodes (4): CaseElement, m_else_body, m_entries, m_value

### Community 738 - "decompiler/IR2: GetMethodElement"
Cohesion: 0.20
Nodes (4): GetMethodElement, m_in, m_is_object, m_name

### Community 739 - "decompiler/IR2: ReturnElement"
Cohesion: 0.20
Nodes (4): ReturnElement, dead_code, return_code, return_type

### Community 740 - "decompiler/types2: Kind"
Cohesion: 0.20
Nodes (9): Kind, BLOCK_ENTRY, FIELD_ACCESS, INT_OR_FLOAT, NONE, UNKNOWN_LABEL, UNKNOWN_STACK_STRUCTURE, Tag (+1 more)

### Community 741 - "docs/progress-notes: Collide-Hash Fragment Bo"
Cohesion: 0.24
Nodes (10): Collide Hash Bucket Array (3D grid of index/count entries), Collide-Cache Triangle Limit (460) and print-exceeded-max-cache-tris, collide-hash, collide-hash-fragment (pat-array, bucket-array, poly array, vert array, index-array), collide-hash-item, Collide-Hash Fragment Bounding-Box Query (annotated asm), *collide-stats*, pat (Surface Attribute) Ignore-Mask Filter (+2 more)

### Community 742 - "docs: OpenGoal Documentation H"
Cohesion: 0.29
Nodes (10): AI Agent and Developer Guide (AGENTS.md), OpenGoal Documentation Hub, GitHub Actions Workflows Guide, How to Create a Mod guide, Lisp Wiki (.agents/skills/goal-lisp/wiki), docs/modding (modding documentation and tool guides), Modular Skills (.agents/skills: goal-lisp, engine-internals, custom-actors-levels, texture-modding, documentalist, kb), Repository Workflow Guide (+2 more)

### Community 743 - "game/graphics: TextureVRAMReference"
Cohesion: 0.20
Nodes (9): Mt4hhTexture, ref, slot, TextureData, data, gl, TextureVRAMReference, gpu_texture (+1 more)

### Community 744 - "game/kernel: SpeedrunPracticeState"
Cohesion: 0.20
Nodes (9): SpeedrunPracticeState, average_time, current_session_id, fastest_time, session_attempts, session_successes, total_attempts, total_successes (+1 more)

### Community 745 - "game/kernel: SpeedrunPracticeState"
Cohesion: 0.20
Nodes (9): SpeedrunPracticeState, average_time, current_session_id, fastest_time, session_attempts, session_successes, total_attempts, total_successes (+1 more)

### Community 746 - "game/mips2c: jak1_functions/collide_e"
Cohesion: 0.24
Nodes (7): Cache, collide_edge_hold_list, collide_edge_work, format, execute(), sub_l16_b15(), sub_l20_b26()

### Community 747 - "game/mips2c: Cache"
Cohesion: 0.20
Nodes (7): Cache, font12_table, font24_table, font_work, math_camera, video_parms, execute()

### Community 748 - "game/mips2c: Cache"
Cohesion: 0.20
Nodes (7): Cache, cheat_mode, collide_stats, debug, fake_scratchpad_data, print_exceeded_max_cache_tris, execute()

### Community 749 - "game/mips2c: Cache"
Cohesion: 0.20
Nodes (7): Cache, font12_table, font24_table, font_work, math_camera, video_params, execute()

### Community 750 - "game/mips2c: Cache"
Cohesion: 0.20
Nodes (7): Cache, cheat_mode, collide_stats, debug, fake_scratchpad_data, print_exceeded_max_cache_tris, execute()

### Community 751 - "game/mips2c: Cache"
Cohesion: 0.20
Nodes (7): Cache, font12_table, font24_table, font_work, math_camera, video_params, execute()

### Community 752 - "game/mips2c: Cache"
Cohesion: 0.20
Nodes (7): Cache, cheat_mode, collide_stats, debug, fake_scratchpad_data, print_exceeded_max_cache_tris, execute()

### Community 753 - "game/overlord: CMsg"
Cohesion: 0.20
Nodes (8): CMsg, data, m_msg, m_ret, m_thread, MsgKind, CANCEL_READ, READ_RAW

### Community 754 - "game/overlord: EIsoStatus"
Cohesion: 0.20
Nodes (10): EIsoStatus, ERROR_b, ERROR_NO_FILE, ERROR_NO_SOUND, ERROR_OPENING_FILE_8, FAILED_TO_QUEUE_4, IDLE_1, NONE_0 (+2 more)

### Community 755 - "game/overlord: Rpc_Player_Base_Cmd"
Cohesion: 0.22
Nodes (8): Rpc_Loader_Set_Mirror_Mode, mode, Rpc_Player_Base_Cmd, command, rsvd1, Rpc_Player_Set_Fps_Cmd, fps, pad

### Community 756 - "game/overlord: EIsoStatus"
Cohesion: 0.20
Nodes (10): EIsoStatus, ERROR_b, ERROR_NO_FILE, ERROR_NO_SOUND, ERROR_OPENING_FILE_8, FAILED_TO_QUEUE_4, IDLE_1, NONE_0 (+2 more)

### Community 757 - "game/sce: sceCdCLOCK"
Cohesion: 0.20
Nodes (9): sceCdCLOCK, day, hour, minute, month, second, stat, week (+1 more)

### Community 758 - "game/sound: HandlePluginMessage()"
Cohesion: 0.31
Nodes (3): HandlePluginMessage(), LogPluginMessage(), RegisterPluginHandler()

### Community 759 - "goalc/emitter: ObjectFileData"
Cohesion: 0.22
Nodes (4): ObjectFileData, header, link_tables, segment_data

### Community 760 - ".agents/skills: Ghost memory pitfall of "
Cohesion: 0.33
Nodes (3): Verification gate function (identify, run, read, verify, claim), Rationalization prevention table, Red flags that signal unverified claims

### Community 761 - "common/cross_os_debug: Kind"
Cohesion: 0.22
Nodes (9): Kind, BREAK, DISAPPEARED, EXCEPTION, ILLEGAL_INSTR, MATH_EXCEPTION, NOTHING, SEGFAULT (+1 more)

### Community 762 - "decompiler/analysis: JumpTableBlock"
Cohesion: 0.22
Nodes (9): JumpTableBlock, branch_always, branch_likely, end_instr, has_branch, idx, start_instr, succ_branch (+1 more)

### Community 763 - "decompiler/data: data/dir_tpages.cpp"
Cohesion: 0.28
Nodes (4): DirTpageResult, lengths, ObjectFileData, process_dir_tpages()

### Community 764 - "decompiler/data: LinkedWordReader"
Cohesion: 0.28
Nodes (3): LinkedWordReader, m_offset, m_words

### Community 765 - "decompiler/level_extractor: ArtJointAnim"
Cohesion: 0.22
Nodes (8): ArtJointAnim, artist_base, artist_step, blend_shape_data, frames, length, name, speed

### Community 766 - "decompiler/types2: Decompiler type pass v2"
Cohesion: 0.33
Nodes (9): Guess function names (planned), Guess types from inspect methods (planned), Type Pass Version 2 design notes, Ambiguous inline structure access uses casts problem, Ambiguous types and constraint resolution, Type of result in cond as value, Automatic guessing of stack and label types, Decompiler type pass v2 (+1 more)

### Community 767 - "docs/img: Launcher mod page screen"
Cohesion: 0.33
Nodes (9): Launcher mod page screenshot (add_mod_5), Jak II sidebar tab (selected), MODS sidebar tab (launcher), OpenGOAL Launcher v2.11.1, Peaceful Haven City (Freedom Fighters) mod, v1.0.0, Play (Jouer) button, highlighted, In-game Mods menu screenshot (add_mod_6), crimson-blueguard-peaceful menu entry (+1 more)

### Community 768 - "docs/scratch: shrub-do-init-frame"
Cohesion: 0.22
Nodes (9): Sprite DMA Packet Sequence, Float Address Trick (floats whose low 16 bits equal VU memory addresses), shrub-do-init-frame, shrub-init-frame, shrub-init-view-data (texture-giftag, fog constants, float address trick constants), *shrub-state* VU Buffer Toggle (164 minus state, base/offset 0), shrub-upload-model, shrub-upload-view-data (+1 more)

### Community 769 - "docs/progress-notes: Jak 1 TFRAG VU1 Micropro"
Cohesion: 0.25
Nodes (9): Debug: Bad adgif A+D Register Data, Debug: Bad Texture Coordinates (q = 4.48), Debug: Zero Coords After Kicking Zone (sps), TFRAG Common Kicking Zone, TFRAG Program 4, TFRAG Program 6 (two versions selected by vi14), TFRAG Program Entry Table (init-globals, reset VF04, branch per mode), Jak 1 TFRAG VU1 Microprograms (+1 more)

### Community 770 - "game/common: Language"
Cohesion: 0.22
Nodes (9): Language, English, French, German, Italian, Japanese, Portuguese, Spanish (+1 more)

### Community 771 - "game/graphics: SpriteDataMem"
Cohesion: 0.22
Nodes (9): SpriteDataMem, Adgif, Buffer0, Buffer1, FrameData, GiftagBuilding, Header, Matrix (+1 more)

### Community 772 - "game/kernel: SpeedrunCustomCategoryEn"
Cohesion: 0.22
Nodes (8): SpeedrunCustomCategoryEntry, cheats, completed_task, continue_point_name, features, forbidden_features, name, secrets

### Community 773 - "game/kernel: SpeedrunCustomCategory"
Cohesion: 0.22
Nodes (7): SpeedrunCustomCategory, cheats, completed_task, features, forbidden_features, index, secrets

### Community 774 - "game/kernel: SpeedrunCustomCategoryEn"
Cohesion: 0.22
Nodes (9): SpeedrunCustomCategoryEntry, cheats, completed_task, continue_point_name, features, forbidden_features, name, secrets (+1 more)

### Community 775 - "game/mips2c: jakx_functions/spatial_h"
Cohesion: 0.22
Nodes (6): Cache, debug_segment, format, mem_copy, perf_stats, execute()

### Community 776 - "game/overlord: FileCacheEntry"
Cohesion: 0.22
Nodes (6): FileCacheEntry, def, fp, last_use_count, offset_in_file, size

### Community 777 - "game/overlord: jak3/iso.h"
Cohesion: 0.22
Nodes (8): CopyKind, EE, IOP, SBK, ISO_VAGCommand, ISOFileDef, RPC_Dgo_Cmd, VagStreamData

### Community 778 - "game/overlord: ISO_LoadCommon"
Cohesion: 0.22
Nodes (8): ISO_LoadCommon, addr, dest_ptr, length_to_copy, maxlen, progress_bytes, ISO_LoadSingle, sector_offset

### Community 779 - "game/overlord: RPC_Dgo_Cmd"
Cohesion: 0.22
Nodes (9): RPC_Dgo_Cmd, buffer1, buffer2, buffer_heap_top, cgo_id, name, pad, rsvd (+1 more)

### Community 780 - "game/overlord: jakx/iso.h"
Cohesion: 0.22
Nodes (8): CopyKind, EE, IOP, SBK, ISO_VAGCommand, ISOFileDef, RPC_Dgo_Cmd, VagStreamData

### Community 781 - "game/overlord: ISO_LoadCommon"
Cohesion: 0.22
Nodes (8): ISO_LoadCommon, addr, dest_ptr, length_to_copy, maxlen, progress_bytes, ISO_LoadSingle, sector_offset

### Community 782 - "game/overlord: RPC_Dgo_Cmd"
Cohesion: 0.22
Nodes (9): RPC_Dgo_Cmd, buffer1, buffer2, buffer_heap_top, cgo_id, name, pad, rsvd (+1 more)

### Community 783 - "game/overlord: CacheEntry"
Cohesion: 0.22
Nodes (7): CacheEntry, countdown, filedef, header, StrFileHeader, sectors, sizes

### Community 784 - "goalc/build_level: Tie.cpp"
Cohesion: 0.42
Nodes (4): add_prototype_array_tie(), add_proxy_prototype_array_tie(), add_tie_tree_to_object_file(), DrawableTreeInstanceTie

### Community 785 - "goal_src/user: User Profiles README"
Cohesion: 0.31
Nodes (8): User Profiles README, repl-config.json (REPL settings, keybinds, per-game history), og:run-below-on-listen marker, startup.gc, User profile directories, user.gs and user.gc scripts, user.txt auto-login, Debugger and listener

### Community 786 - "goalc/emitter: Flags"
Cohesion: 0.22
Nodes (9): Flags, kIsNull, kOp2Set, kOp3Set, kSetDispImm, kSetImm, kSetModrm, kSetRex (+1 more)

### Community 787 - "goalc/make: .get_additional_dependen"
Cohesion: 0.31
Nodes (4): DgoTool, m_reader, parse_desc_file(), parse_name_list()

### Community 788 - "goalc/regalloc: AssignmentRange"
Cohesion: 0.25
Nodes (5): AssignmentRange, m_ass, m_end, m_live, m_start

### Community 789 - "goalc/regalloc: Op"
Cohesion: 0.25
Nodes (6): Op, load, reg, reg_class, slot, store

### Community 790 - "lsp/handlers: text_document/document_s"
Cohesion: 0.39
Nodes (6): did_change(), did_change_push_diagnostics(), did_close(), did_open(), did_open_push_diagnostics(), will_save()

### Community 791 - "lsp/state: OGGlobalIndex"
Cohesion: 0.22
Nodes (7): OGGlobalIndex, global_symbols, per_file_symbols, OpenGOALFormResult, end_point, start_point, tokens

### Community 792 - ".agents/skills: 2-circuit architecture f"
Cohesion: 0.36
Nodes (4): Decompiler asset pipeline workflow, Texture extraction and baking workflow, Texture image specifications (RGBA PNG), Texture replacement directory structure (texture_replacements, _all, texture_merges)

### Community 793 - "common/goos: ShortInfo"
Cohesion: 0.25
Nodes (7): ShortInfo, filename, line_idx_to_display, line_text, pos_in_line, GlobalConstantInfo, definition_info

### Community 794 - "common: ListenerToTargetMsgKind"
Cohesion: 0.25
Nodes (8): ListenerToTargetMsgKind, LTT_MSG_CODE, LTT_MSG_INSPECT, LTT_MSG_POKE, LTT_MSG_PRINT, LTT_MSG_PRINT_SYMBOLS, LTT_MSG_RESET, LTT_MSG_SHUTDOWN

### Community 796 - "docs/scratch: Sprite Distort VU1 Micro"
Cohesion: 0.32
Nodes (6): Sprite Distort VU1 Microcode, Sine Tables (entry, ientry, giftag, color), Sprite flag = slice count (3-11), VU1 Memory Layout (sprite distort), OpenGL renderer sources, Sprite3 Distort renderer

### Community 797 - "game/graphics: FramePlot"
Cohesion: 0.25
Nodes (6): FramePlot, m_buffer, m_idx, SIZE, SmallProfiler, m_plots

### Community 798 - "game/graphics: SkyInput"
Cohesion: 0.25
Nodes (8): SkyInput, cloud_dest, cloud_max, cloud_min, fog_height, max_times, scales, times

### Community 799 - "game/mips2c: jak1_functions/collide_f"
Cohesion: 0.25
Nodes (5): Cache, collide_do_primitives, ray_cylinder_intersect, ray_sphere_intersect, execute()

### Community 800 - "game/mips2c: jak1_functions/generic_e"
Cohesion: 0.32
Nodes (5): Cache, fake_scratchpad_data, execute(), vcallms0(), vcallms48()

### Community 801 - "game/mips2c: Cache"
Cohesion: 0.25
Nodes (6): Cache, blerc_globals, fake_scratchpad_data, flush_cache, gsf_buffer, stats_blerc

### Community 802 - "game/mips2c: Cache"
Cohesion: 0.25
Nodes (8): Cache, clip_polygon_against_negative_hyperplane, clip_polygon_against_positive_hyperplane, draw_boundary_polygon, draw_large_polygon, fake_scratchpad_data, math_camera, sky_tng_data

### Community 803 - "game/mips2c: jak2_functions/collide_f"
Cohesion: 0.25
Nodes (5): Cache, collide_do_primitives, ray_cylinder_intersect, ray_sphere_intersect, execute()

### Community 804 - "game/mips2c: jak2_functions/spatial_h"
Cohesion: 0.25
Nodes (5): Cache, mem_copy, perf_stats, vector_vector_distance_squared, execute()

### Community 805 - "game/mips2c: jak3_functions/collide_f"
Cohesion: 0.25
Nodes (5): Cache, collide_do_primitives, ray_cylinder_intersect, ray_sphere_intersect, execute()

### Community 806 - "game/mips2c: jak3_functions/spatial_h"
Cohesion: 0.25
Nodes (5): Cache, mem_copy, perf_stats, vector_vector_distance_squared, execute()

### Community 807 - "game/mips2c: jak3_functions/wvehicle_"
Cohesion: 0.25
Nodes (5): Cache, atan, target, transform_point_qword, execute()

### Community 808 - "game/mips2c: jakx_functions/collide_f"
Cohesion: 0.25
Nodes (5): Cache, collide_do_primitives, ray_cylinder_intersect, ray_sphere_intersect, execute()

### Community 809 - "game/mips2c: Cache"
Cohesion: 0.25
Nodes (6): Cache, blerc_globals, fake_scratchpad_data, flush_cache, gsf_buffer, stats_blerc

### Community 810 - "game/mips2c: jakx_functions/wvehicle_"
Cohesion: 0.25
Nodes (5): Cache, atan, transform_point_qword, view_get_active_target, execute()

### Community 811 - "game/mips2c: Mips2C README"
Cohesion: 0.43
Nodes (8): Mips2C README, draw-string (reference Mips2C function), ExecutionContext and fake stack (mips2c_call_systemv), __pc-get-mips2c GOAL accessor, hacks.jsonc mips2c function list, Mips2C limitations, gMips2CLinkCallbacks and link() mechanism, Mips2C converter

### Community 812 - "game/overlord: Rpc_Player_Set_Ear_Trans"
Cohesion: 0.25
Nodes (8): Rpc_Player_Set_Ear_Trans_Cmd, cam_forward, cam_inverted, cam_left, cam_scale, ear_trans, ear_trans0, ear_trans1

### Community 813 - "game/overlord: RPC_Str_Cmd"
Cohesion: 0.25
Nodes (8): RPC_Str_Cmd, address, basename, dummy, maxlen, result, rsvd, section

### Community 814 - "game/overlord: RPC_Str_Cmd"
Cohesion: 0.25
Nodes (8): RPC_Str_Cmd, address, basename, dummy, maxlen, result, rsvd, section

### Community 815 - "goalc/emitter: Info"
Cohesion: 0.25
Nodes (5): Info, call_preserved_bytes, name, saved, special

### Community 816 - "lsp: lsp executable (OpenGOAL"
Cohesion: 0.25
Nodes (7): lsp executable (OpenGOAL language server), MIPS instruction data for LSP, LSP protocol types, LSP stdio transport, LSP text_document handlers (completion, hover, go-to, formatting, symbols, colors, type hierarchy), tree-sitter parser dependency, LSP workspace state and requester

### Community 817 - "common/sqlite: GenericResponse"
Cohesion: 0.29
Nodes (4): GenericResponse, rows, run_sql_query(), run_sql_query()

### Community 818 - "common/type_system: parse_defenum()"
Cohesion: 0.48
Nodes (4): cdr(), is_type(), parse_defenum(), symbol_string()

### Community 819 - "common/type_system: DeftypeResult"
Cohesion: 0.29
Nodes (6): DeftypeResult, create_runtime_type, flags, type, type_info, TypeFlags

### Community 820 - "decompiler/analysis: Register"
Cohesion: 0.29
Nodes (4): Entry, entry_id, reg, var_id

### Community 821 - "decompiler/Function: Break"
Cohesion: 0.29
Nodes (4): Break, body, dest_block_id, unreachable_block

### Community 822 - "decompiler/Function: DelaySlotKind"
Cohesion: 0.29
Nodes (7): DelaySlotKind, NO_BRANCH, NO_DELAY, NOP, OTHER, SET_REG_FALSE, SET_REG_TRUE

### Community 823 - "decompiler/level_extractor: CompressedFrame"
Cohesion: 0.29
Nodes (4): CompressedFrame, data16, data32, data64

### Community 824 - "docs/img: .zed/debug.json debug co"
Cohesion: 0.33
Nodes (7): Zed editor debug task picker screenshot, .zed/debug.json debug configurations, Zed Debug tab task picker (Run / Debug / Attach / Launch), Game - Jak 1/2/3 (Windows) debug tasks, REPL - Jak 1/2/3 (Windows) debug tasks, Tests - Unit - Draft Only (Windows) debug task, Zed editor

### Community 825 - "game/graphics: SpriteProgMem"
Cohesion: 0.29
Nodes (7): SpriteProgMem, Init, Sprites2dGrp0, Sprites2dHud_Jak1, Sprites2dHud_Jak2, Sprites2dHud_Jak3, Sprites3d

### Community 826 - "game/kernel: SQLResult"
Cohesion: 0.29
Nodes (5): SQLResult, allocated_length, data, error, len

### Community 827 - "game/kernel: jak3/kmalloc.cpp"
Cohesion: 0.29
Nodes (3): kmemclose(), kmemopen(), kmemopen_from_c()

### Community 828 - "game/kernel: jakx/kmalloc.cpp"
Cohesion: 0.29
Nodes (3): kmemclose(), kmemopen(), kmemopen_from_c()

### Community 829 - "game/mips2c: collide_probe.cpp"
Cohesion: 0.29
Nodes (4): Cache, collide_probe_stack, collide_work, execute()

### Community 830 - "game/mips2c: Cache"
Cohesion: 0.29
Nodes (7): Cache, clear_frame_accumulator, decompress_fixed_data_to_accumulator, decompress_frame_data_pair_to_accumulator, decompress_frame_data_to_accumulator, fake_scratchpad_data, normalize_frame_quaternions

### Community 831 - "game/overlord: VagCmdByte"
Cohesion: 0.29
Nodes (7): VagCmdByte, BYTE10, BYTE11, BYTE23_NOSTART, BYTE4, BYTE5, BYTE6

### Community 832 - "game/overlord: ISOFileDef"
Cohesion: 0.29
Nodes (5): ISOFileDef, full_path, name, ISOName, data

### Community 833 - "game/overlord: RpcId"
Cohesion: 0.29
Nodes (7): RpcId, DGO, Loader, LoadToEE, PLAY, Player, STR

### Community 834 - "game/overlord: ISOFileDef"
Cohesion: 0.29
Nodes (5): ISOFileDef, full_path, name, ISOName, data

### Community 835 - "game/overlord: RpcId"
Cohesion: 0.29
Nodes (7): RpcId, DGO, Loader, LoadToEE, PLAY, Player, STR

### Community 839 - "game/system: State"
Cohesion: 0.29
Nodes (7): State, Dormant, Ready, Run, Suspend, Wait, WaitSuspend

### Community 840 - "goalc/emitter: VF_ELEMENT"
Cohesion: 0.29
Nodes (7): IR_SplatVF::IR_SplatVF(), VF_ELEMENT, NONE, W, X, Y, Z

### Community 841 - "goalc/compiler: Kind"
Cohesion: 0.29
Nodes (7): Kind, CONSTANT_DATA, FUNCTION_REFERENCE, INVALID, STRUCTURE_REFERENCE, SYMBOL, TYPE

### Community 842 - "goalc/compiler: ArgumentInfo"
Cohesion: 0.29
Nodes (7): ArgumentInfo, description, is_mutated, is_optional, is_unused, name, type

### Community 843 - "goalc/compiler: FieldInfo"
Cohesion: 0.29
Nodes (7): FieldInfo, description, is_array, is_dynamic, is_inline, name, type

### Community 844 - "goalc/compiler: ValOrConstant"
Cohesion: 0.33
Nodes (3): ValOrConstant, constant, val

### Community 845 - "lsp/handlers: text_document/type_hiera"
Cohesion: 0.48
Nodes (3): prepare_type_hierarchy(), subtypes_type_hierarchy(), supertypes_type_hierarchy()

### Community 846 - "test/goalc: SharedCompiler"
Cohesion: 0.29
Nodes (4): SharedCompiler, compiler, runner, runtime_thread

### Community 847 - ".agents/skills: Lisp wiki common.md (all"
Cohesion: 0.53
Nodes (6): Lisp wiki common.md (all games), OpenGOAL Lisp Wiki (verified source of truth for GOAL code), Lisp wiki jak1.md, Lisp wiki jak2.md, Lisp wiki jak3.md, kb skill

### Community 848 - ".agents/skills: Context pointers"
Cohesion: 0.40
Nodes (5): Context pointers, Leading words, Skill invocation choice (model-invoked vs user-invoked), Router skills, The two loads (context load and cognitive load)

### Community 849 - "common: RegClass"
Cohesion: 0.33
Nodes (6): RegClass, FLOAT, GPR_64, INT_128, INVALID, VECTOR_FLOAT

### Community 850 - "common/type_system: FieldLookupInfo"
Cohesion: 0.33
Nodes (5): FieldLookupInfo, array_size, field, needs_deref, type

### Community 851 - "common/versions: versions.cpp"
Cohesion: 0.47
Nodes (3): valid_game_version(), valid_game_version_names(), version_to_game_name_external()

### Community 853 - "decompiler/Function: WhileLoop"
Cohesion: 0.33
Nodes (3): WhileLoop, body, condition

### Community 854 - "decompiler/level_extractor: JointAnimCompressedContr"
Cohesion: 0.33
Nodes (6): JointAnimCompressedControl, fixed, fixed_qwc, frame, frame_qwc, num_frames

### Community 856 - "decompiler/VuDisasm: VuLowerOp6"
Cohesion: 0.33
Nodes (4): VuLowerOp6, goto_other, kind, known

### Community 857 - "docs/progress-notes: asm-near (near DMA gener"
Cohesion: 0.33
Nodes (6): asm-near (near DMA generation asm), HFrag DMA Generation Asms (near, near-mid, mid, far-mid, far, far-scissor, near-mid-scissor), hfrag generate-dma, poly9 DMA-from-spr Vertex Order ((0,3,1,4), (1,4,2,5), (3,6,4,7), (4,7,5,8)), HFrag Vertex Morph: weight*vt0 + (1-weight)*0.5*(vt1+vt2), HFrag VU1 Program Addresses (init, abort, poly4-near, poly25-far/mid, poly9-mid/near)

### Community 858 - "game/graphics: ProfilerStats"
Cohesion: 0.33
Nodes (4): ProfilerStats, draw_calls, duration, triangles

### Community 859 - "game/graphics: ProfilerSort"
Cohesion: 0.33
Nodes (5): ProfilerSort, DRAW_CALLS, NONE, TIME, TRIANGLES

### Community 860 - "game/kernel: SQLResult"
Cohesion: 0.33
Nodes (4): SQLResult, allocated_length, error, len

### Community 864 - "game/mips2c: jak1_functions/collide_m"
Cohesion: 0.33
Nodes (3): Cache, closest_pt_in_triangle, execute()

### Community 865 - "game/mips2c: test_func.cpp"
Cohesion: 0.33
Nodes (3): Cache, goal_check_function, execute()

### Community 866 - "game/mips2c: jak2_functions/collide_m"
Cohesion: 0.33
Nodes (3): Cache, closest_pt_in_triangle, execute()

### Community 867 - "game/mips2c: jak2_functions/lights.cp"
Cohesion: 0.33
Nodes (3): Cache, light_hash_work, execute()

### Community 868 - "game/mips2c: jak3_functions/collide_m"
Cohesion: 0.33
Nodes (3): Cache, closest_pt_in_triangle, execute()

### Community 869 - "game/mips2c: Cache"
Cohesion: 0.33
Nodes (6): Cache, blerc_globals, fake_scratchpad_data, flush_cache, gsf_buffer, stats_blerc

### Community 870 - "game/mips2c: jak3_functions/particle_"
Cohesion: 0.33
Nodes (3): Cache, random_generator, execute()

### Community 871 - "game/mips2c: jakx_functions/lights.cp"
Cohesion: 0.33
Nodes (3): Cache, light_hash_work, execute()

### Community 872 - "game/mips2c: jakx_functions/particle_"
Cohesion: 0.33
Nodes (3): Cache, random_generator, execute()

### Community 873 - "game/overlord: jak3/iso_queue.h"
Cohesion: 0.40
Nodes (5): ISO_Hdr, ISO_VAGCommand, PriStackEntry, cmds, count

### Community 874 - "game/overlord: VagDir"
Cohesion: 0.33
Nodes (6): VagDir, entries, num_entries, vag_magic_1, vag_magic_2, vag_version

### Community 875 - "game/overlord: BufferType"
Cohesion: 0.33
Nodes (6): BufferType, EBT_FREE, NORMAL, REQUEST_NORMAL, REQUEST_VAG, VAG

### Community 876 - "game/overlord: jakx/iso_queue.h"
Cohesion: 0.40
Nodes (5): ISO_Hdr, ISO_VAGCommand, PriStackEntry, cmds, count

### Community 877 - "game/overlord: VagDir"
Cohesion: 0.33
Nodes (6): VagDir, entries, num_entries, vag_magic_1, vag_magic_2, vag_version

### Community 878 - "game/overlord: BufferType"
Cohesion: 0.33
Nodes (6): BufferType, EBT_FREE, NORMAL, REQUEST_NORMAL, REQUEST_VAG, VAG

### Community 879 - "goalc/compiler: DebugStats"
Cohesion: 0.33
Nodes (6): DebugStats, funcs_requiring_v1_allocator, num_moves_eliminated, num_spills, num_spills_v1, total_funcs

### Community 880 - "goalc/compiler: Settings"
Cohesion: 0.33
Nodes (6): Settings, allow_inline, inline_by_default, is_set, print_asm, save_code

### Community 881 - "goalc/data_compiler: compile_game_text()"
Cohesion: 0.53
Nodes (5): compile_game_subtitles(), compile_game_text(), compile_subtitles_v1(), compile_subtitles_v2(), compile_text()

### Community 884 - "common/formatter: Triangle of Death diagra"
Cohesion: 0.60
Nodes (5): Triangle of Death diagram (formatter docs), Vertical indentation guide lines, OpenGOAL Lisp code formatter, Rainbow bracket coloring, Triangle of death (stacked closing parens staircase)

### Community 885 - "common/type_system: BitfieldLookupInfo"
Cohesion: 0.40
Nodes (5): BitfieldLookupInfo, offset, result_type, sign_extend, size

### Community 887 - "common/util: Filtered"
Cohesion: 0.50
Nodes (3): Filtered, m_alpha, m_val

### Community 888 - "decompiler/analysis: insert_lets.h"
Cohesion: 0.40
Nodes (3): LetStats, total_vars, vars_in_lets

### Community 889 - "decompiler: RegisterTypeCast"
Cohesion: 0.40
Nodes (4): RegisterTypeCast, atomic_op_idx, reg, type_name

### Community 894 - "game/graphics: DsFbo"
Cohesion: 0.40
Nodes (4): DsFbo, fbo, size, tex

### Community 895 - "game/graphics: SpriteRecord"
Cohesion: 0.40
Nodes (4): SpriteRecord, draw_mode, idx, tbp

### Community 896 - "game/overlord: State"
Cohesion: 0.40
Nodes (5): State, ACTIVE, READ_DONE, READING, UNMAKRED

### Community 897 - "game/overlord: State"
Cohesion: 0.40
Nodes (5): State, ACTIVE, READ_DONE, READING, UNMAKRED

### Community 898 - "goalc/build_sbk: TailGrowResult"
Cohesion: 0.40
Nodes (5): TailGrowResult, bytes, grew_names, patched_sfxud, sfxud_rel

### Community 899 - "goalc/emitter: StaticData"
Cohesion: 0.40
Nodes (4): StaticData, data, location, min_align

### Community 900 - "goalc/retarget_anim: RetargetOptions"
Cohesion: 0.40
Nodes (4): RetargetOptions, force_180_yaw_align_anim, force_neutral_scale_joints, root_joints

### Community 901 - "scripts/gsrc: iteratively-copy-decomp."
Cohesion: 0.60
Nodes (3): copy_casts(), main(), process_entry()

### Community 902 - "scripts: Korean jamo glyph atlas"
Cohesion: 0.60
Nodes (5): Korean jamo glyph atlas, font.24hi2 glyph page (indices 306-3ff), font.24hi glyph page (indices x186-x18B), Hex glyph index labels, Hangul jamo (consonant and vowel components)

### Community 904 - ".agents/skills: Process life cycle"
Cohesion: 0.50
Nodes (3): Processes and behaviors, Process life cycle, Send an event (send-event)

### Community 905 - ".agents/skills: Memory constants (EE_MAI"
Cohesion: 0.67
Nodes (4): Memory constants (EE_MAIN_MEM_SIZE, END_OF_MEMORY, DEBUG_LEVEL_HEAP_MULT), Jak 1 memory configuration, Jak 2 memory configuration (DEBUG_LEVEL_HEAP_MULT 12.0), Jak 3 memory configuration (DEBUG_LEVEL_HEAP_MULT 15.0)

### Community 907 - "game/common: GameLaunchOptions"
Cohesion: 0.50
Nodes (4): GameLaunchOptions, disable_display, game_version, server_port

### Community 908 - "game/graphics: SmallProfilerStats"
Cohesion: 0.50
Nodes (4): SmallProfilerStats, draw_calls, time_per_category, triangles

### Community 909 - "game/kernel: u64"
Cohesion: 0.50
Nodes (3): AutoSplitterBlock, marker, pointer_to_symbol

### Community 910 - "game/overlord: FakeIsoEntry"
Cohesion: 0.50
Nodes (3): FakeIsoEntry, full_path, iso_name

### Community 911 - "game/overlord: RamdiskFileRecord"
Cohesion: 0.50
Nodes (4): RamdiskFileRecord, additional_offset, file_id, size

### Community 912 - "game/overlord: SoundRpcCommand"
Cohesion: 0.50
Nodes (3): SoundRpcCommand, j2command, rsvd1

### Community 913 - "game/overlord: DgoFno"
Cohesion: 0.50
Nodes (4): DgoFno, CANCEL, LOAD, LOAD_NEXT

### Community 914 - "goalc/build_sbk: V2GrainEntries"
Cohesion: 0.50
Nodes (4): V2GrainEntries, grain_data_bytes, grain_table_bytes, sound_bytes

### Community 916 - "goalc/debugger: StepKind"
Cohesion: 0.50
Nodes (4): StepKind, INTO, OUT_OF, OVER

### Community 917 - "goalc/emitter: PointerLink"
Cohesion: 0.50
Nodes (4): PointerLink, dest, segment, source

### Community 918 - "goalc/regalloc: Kind"
Cohesion: 0.50
Nodes (4): Kind, REGISTER, STACK, UNASSIGNED

### Community 919 - "misc: blender-mcp"
Cohesion: 0.50
Nodes (3): uvx, blender-mcp, blender-mcp

### Community 920 - ".agents/skills: Jak 3 has no custom art-"
Cohesion: 1.00
Nodes (3): Master art group and animation slot mapping, Custom art-groups and dynamic animation linking (link-art!), Jak 3 has no custom art-group dynamic linking hook

### Community 921 - ".agents/skills: PC settings and cheats p"
Cohesion: 0.67
Nodes (3): PC settings and cheats persistence (pc-settings.gc), Save Slot 1 auto-load on cold boot, Secrets menu (game-secrets bitfield)

### Community 922 - ".agents/skills: Jak 3 powers and weapons"
Cohesion: 0.67
Nodes (3): Dark Jak stages (darkjak-stage bitfield), Jak 3 powers and weapons interplay, Jak 3 weapon system (gun)

### Community 923 - ".agents/skills: When to split a document"
Cohesion: 0.67
Nodes (3): Steps and completion criteria (clarity and demand), Splitting by invocation, When to split a document (by sequence or invocation)

### Community 924 - "docs/img: Robot guard model render"
Cohesion: 0.67
Nodes (3): Robot guard model render, Spiked spherical robot design, Twin side cannons and glass eye lens

### Community 925 - "docs/progress-notes: HFrag Montage Texture (1"
Cohesion: 0.67
Nodes (3): hfragment login Method (adgif-shader-login for 3 shaders), hfragment Method 23 (near texture / montage DMA generation), HFrag Montage Texture (16x8 grid) and Near Texture Data

### Community 926 - "docs/scratch: draw-drawable-tree-insta"
Cohesion: 0.67
Nodes (3): draw-drawable-tree-instance-shrub, draw-inline-array-instance-shrub, draw-prototype-inline-array-shrub

### Community 927 - "goalc/data_compiler: PointerLinkRecord"
Cohesion: 0.67
Nodes (3): PointerLinkRecord, source_word, target_byte

## Ambiguous Edges - Review These
- `generic-tie-normal type (int8 x y z)` → `Wrong-normals bug on a few fragments (index_table, normal scale)`  [AMBIGUOUS]
  docs/progress-notes/jak1/scratch/generic_tie_to_etie.md · relation: conceptually_related_to
- `task update-ref-tests (regenerate all _REF.gc references)` → `--dump-mode flag and failures folder`  [AMBIGUOUS]
  Taskfile.yml · relation: conceptually_related_to
- `Installed mods section (Mods installes)` → `Header status: Mod Version Not installed!`  [AMBIGUOUS]
  docs/img/add_mod_2.png · relation: conceptually_related_to

## Knowledge Gaps
- **13515 isolated node(s):** `extract_build_unix.sh script`, `extract_build_windows.sh script`, `uvx`, `blender-mcp`, `endOfLine` (+13510 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 18266 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **83 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `generic-tie-normal type (int8 x y z)` and `Wrong-normals bug on a few fragments (index_table, normal scale)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `task update-ref-tests (regenerate all _REF.gc references)` and `--dump-mode flag and failures folder`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Installed mods section (Mods installes)` and `Header status: Mod Version Not installed!`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `vector` connect `Form Expression Analysis` to `Game Kernel Runtime`, `x86 Emitter and Codegen`, `Tfrag3 and TIE Data`, `Compiler IR and Regalloc`, `Decompiler Utilities`, `Listener and Sockets`, `DMA Follower and Sprite3`, `Compiler Test Runner`, `Compiler Environments`, `Decompiler Form Matching`, `Decompiler Atomic Ops`, `LSP Handlers`, `Compiler Values and Regs`, `Decompiler IR2 Env`, `Decompiler Form Elements`, `Compiler Static Data`, `Texture Animator`, `Offline Test Orchestration`, `Tie3 and Tfrag Renderer`, `Data Decompile and TypeSpec`, `GOOS Interpreter`, `game/graphics: BucketRenderer`, `goalc/compiler: IR.cpp`, `decompiler/analysis: AtomicOp`, `game/graphics: TFragment`, `game/graphics: OpenGLRenderer`, `common/goos: Object`, `decompiler/level_extractor: extract_merc.cpp`, `goalc/build_actor: jak1/build_actor.cpp`, `goalc/build_actor: jak3/build_actor.cpp`, `decompiler/level_extractor: extract_tie.cpp`, `decompiler/IR2: bitfields.cpp`, `goalc/emitter: ObjectGenerator.cpp`, `test/goalc: TEST_F()`, `goalc/build_actor: jak2/build_actor.cpp`, `decompiler/level_extractor: GameVersion`, `game/kernel: cprintf()`, `game/graphics: AdgifHelper`, `decompiler/Function: Function`, `decompiler/analysis: analyze_inspect_method.c`, `decompiler/IR2: StaticInfo`, `goalc/build_level: Region`, `goalc/build_level: Region`, `game/system: mutex`, `decompiler/ObjectFile: ObjectFileDB`, `decompiler/level_extractor: extract_tfrag.cpp`, `goalc/compiler: TypeDocumentation`, `test/decompiler: FormRegressionTest.cpp`, `test/goalc: test_vector_float.cpp`, `game/system: InputBindingGroups`, `common/dma: DrawMode`, `decompiler/level_extractor: Level`, `game/sound: common_types`, `common/type_system: TypeSystem`, `game/system: InputManager`, `decompiler/IR2: FormElement`, `game/sound: SFXBlock`, `test/decompiler: TEST()`, `game/graphics: TextureAnimator.cpp`, `decompiler/level_extractor: MercData.cpp`, `goalc/compiler: Val`, `goalc/build_level: ResLump.cpp`, `game/overlord: jakx/iso_cd.cpp`, `decompiler/data: FakePlayer`, `game/graphics: LoaderInput`, `lsp/state: Workspace`, `decompiler: Config`, `goalc/compiler: Util.cpp`, `goalc/compiler: .get_none()`, `goalc/compiler: compilation/Type.cpp`, `common/custom_data: MercModel`, `decompiler/data: FullGrainInfo`, `game/graphics: EyeRenderer`, `common/util: gltf_util.cpp`, `common/repl: Wrapper`, `game/system: DisplayManager`, `decompiler/types2: SimpleExpression`, `game/graphics: Shadow2`, `goalc/build_level: LevelFile`, `goalc/build_level: LevelFile`, `goalc/regalloc: VarAssignment`, `common/formatter: FormatterTreeNode`, `decompiler/data: game_text.cpp`, `common/log: log.cpp`, `common/util: GameTextFontBank`, `decompiler/level_extractor: array`, `goalc/make: Tools.cpp`, `goalc/build_level: LevelFile`, `common/goos: Reader.cpp`, `common/util: json`, `decompiler/analysis: cfg_builder.cpp`, `goalc/build_level: jak3/collide.cpp`, `goalc/build_level: tfrag3data`, `game/graphics: Hfrag`, `decompiler/extractor: parse_commented_json()`, `decompiler/Disasm: InstructionAtom`, `game/system: SystemThread`, `goalc/emitter: InstructionARM64`, `goalc/regalloc: AllocationInput`, `decompiler/analysis: PrettyPrinter`, `game/graphics: opengl.cpp`, `decompiler/IR2: GenericOperator`, `decompiler/types2: Instruction`, `game/settings: InputSettings`, `game/graphics: Loader`, `goalc/build_level: jak2/collide.cpp`, `goalc/emitter: RegisterInfo`, `game/graphics: ShadowRenderer`, `decompiler/IR2: FormStack.cpp`, `game/graphics: Shrub`, `common/global_profiler: GlobalProfiler`, `common/util: path`, `goalc/make: MakeSystem`, `decompiler/IR2: Entry`, `goalc/build_level: ResLump`, `common/goos: InternedSymbolPtr`, `common/type_system: Type`, `decompiler/data: TexturePage`, `game/graphics: FramebufferTexturePair`, `goalc/build_level: PatSurface`, `goalc/build_level: color_quantization.cpp`, `decompiler/util: DecompilerTypeSystem`, `decompiler/IR2: DerefToken`, `game/graphics: Tree`, `game/graphics: TextureAnimator.h`, `game/sound: MIDISound`, `decompiler/ObjectFile: ObjectFileDB_IR2.cpp`, `decompiler/util: sparticle_decompile.cpp`, `game/graphics: Merc2`, `game/graphics: ClutBlender`, `goalc/emitter: s64`, `goalc/emitter: TEST()`, `common/goos: PrettyPrinterNode`, `game/sound: BinaryReader`, `game/graphics: FixedLayerDef`, `game/overlord: jak3/iso_cd.cpp`, `goalc/build_level: CollideFragMeshData`, `decompiler/data: TextureDB`, `test/goalc: ArithmeticTests`, `game/graphics: DepthCue`, `game/system: MouseDevice`, `game/graphics: GlowRenderer`, `goalc/compiler: .for_each_in_list()`, `decompiler/Disasm: .parse_single_instructio`, `common/serialization: GameSubtitleBank`, `decompiler/IR2: form_as_atom()`, `goalc/debugger: FunctionDebugInfo`, `common/custom_data: TfragTree`, `decompiler/level_extractor: tfrag_tie_fixup.cpp`, `common/type_system: TypeFieldLookup.cpp`, `decompiler/level_extractor: Ref`, `goalc/data_compiler: DataObjectGenerator`, `goalc/regalloc: RegAllocBasicBlock`, `game/sce: sif_ee_memcard.cpp`, `decompiler/ObjectFile: LinkedObjectFileCreation`, `decompiler/types2: types2.cpp`, `goalc/build_level: CollideFragment`, `goalc/build_level: EntityActor`, `goalc/build_level: EntityActor`, `common/goos: Node`, `game/graphics: Draw`, `goalc/build_level: CollideFragment`, `goalc/compiler: SymbolInfo`, `lsp/protocol: CompletionItem`, `goalc/build_actor: NodeWithTransform`, `goalc/build_actor: CompressedAnim`, `decompiler/level_extractor: extract_level.cpp`, `common/goos: SourceText`, `common/serialization: GameSubtitleDefinitionFi`, `test: TEST()`, `common/formatter: FormFormattingConfig`, `game/graphics: Merc2.cpp`, `game/system: IOP`, `goalc/debugger: DebugServer`, `lsp/protocol: Diagnostic`, `common/type_system: StateHandler`, `decompiler/IR2: AtomicOpForm.cpp`, `decompiler/IR2: SimpleExpressionElement`, `decompiler/IR2: Maps`, `goalc/make: Tool`, `tools/memory_dump_tool: memory_dump_tool/main.cp`, `common/texture: process_tpage()`, `common/util: Hunk`, `decompiler/IR2: VariableNames`, `decompiler/VuDisasm: VuDisassembler`, `goalc/build_sbk: GrainData`, `common/custom_data: Vertex`, `common/util: string_util.cpp`, `decompiler/analysis: variable_naming.cpp`, `decompiler/level_extractor: extract_collide_frags()`, `goalc/compiler: algorithm`, `common/type_system: StructureType`, `common/util: read_iso_file.cpp`, `decompiler/Function: ControlFlowGraph`, `decompiler/VuDisasm: VuDisassembler.cpp`, `goalc/build_actor: jak1/build_level.cpp`, `decompiler/analysis: SSA`, `decompiler/Function: CfgVtx`, `decompiler/IR2: LabelInfo`, `decompiler/IR2: VectorFloatLoadStoreElem`, `game/external: discord.cpp`, `game/graphics: MercDebugStats`, `goalc/compiler: SymbolInfoMap`, `goalc/debugger: InstructionPointerInfo`, `goalc/build_actor: animation_processing.cpp`, `common/serialization: subtitles_v2.cpp`, `decompiler/analysis: analyze_ir2_register_usa`, `test: TEST()`, `common/util: font_utils_korean.cpp`, `decompiler/util: StackSpillMap`, `decompiler/IR2: OpenGOALAsm`, `game/graphics: LevelData`, `game/system: KeyboardDevice`, `game/system: IOP_Kernel`, `decompiler/analysis: M2C_Block`, `decompiler/analysis: SymbolMapBuilder`, `common/type_system: FieldReverseLookupOutput`, `decompiler/IR2: ArrayFieldAccess`, `decompiler/ObjectFile: ObjectFileData`, `goalc/build_level: add_actors_from_json()`, `goalc/listener: MemoryMapEntry`, `decompiler/Function: Warnings.h`, `lsp/protocol: TypeHierarchyItem`, `goalc/build_level: collide_bvh.cpp`, `game/graphics: GpuTexture`, `goalc/build_actor: BuildActorParams`, `goalc/regalloc: RACache`, `goalc/build_sbk: build_sbk.cpp`, `common/dma: FixedChunkDmaCopier`, `common/goos: ObjectType`, `decompiler/data: StrFileReader.cpp`, `game/graphics: TextureUploadHandler`, `lsp/protocol: DocumentSymbol`, `decompiler/analysis: get_defstate_entries()`, `goalc/retarget_anim: retarget_anim.cpp`, `decompiler/VuDisasm: .decode()`, `game/kernel: SpeedrunPracticeEntry`, `game/kernel: SpeedrunPracticeEntry`, `goalc/regalloc: LiveInfo`, `lsp/protocol: DidChangeTextDocumentPar`, `common/util: T`, `decompiler/analysis: final_output.cpp`, `game/graphics: SpriteGlowOutput`, `game/kernel: SpeedrunPracticeEntry`, `common/util: BinaryWriter`, `common/util: TrieWithDuplicates`, `goalc/build_level: TieOutput`, `goalc/debugger: disassemble_x86_function`, `decompiler/level_extractor: ProgramInfo`, `decompiler/VuDisasm: VuInstruction`, `game/graphics: TexturePool`, `goalc/build_sbk: SoundData`, `common/math: geometry.h`, `decompiler/ObjectFile: LinkedObjectFile`, `goalc/compiler: Lambda`, `goalc/debugger: u32`, `decompiler/analysis: Mips2C_Output`, `decompiler: DecompileHacks`, `decompiler/level_extractor: JointAnimCompressedFixed`, `game/graphics: CollideMeshRenderer`, `goalc/retarget_anim: SkeletonJoints`, `goalc/emitter: CodeTester.cpp`, `common/sqlite: sqlite.h`, `common/util: BinaryWriter.h`, `common/util: Serializer.h`, `decompiler/Function: CfgVtx.cpp`, `decompiler/analysis: mips2c.cpp`, `decompiler/analysis: run_variable_renaming()`, `decompiler/data: GameCountResult`, `decompiler/level_extractor: JointAnimCompressedFrame`, `common/audio: audio_formats.cpp`, `decompiler/analysis: try_modify_input_types_f`, `decompiler/Function: BasicBlock`, `decompiler/Function: CfgVtx.h`, `decompiler/level_extractor: common_formats.h`, `game/mips2c: Cache`, `game/system: sdl_util.cpp`, `game/tools: Entry`, `test: TEST()`, `common/util: image_resize.cpp`, `decompiler/analysis: FunctionAtomicOps`, `decompiler/Function: Object`, `decompiler/IR2: CondNoElseElement`, `decompiler/IR2: UseDefInfo`, `decompiler/level_extractor: UncompressedJointAnim`, `goalc/build_sbk: create_sbk()`, `decompiler/level_extractor: CompressedAnim`, `decompiler/level_extractor: MercSwapInfo`, `decompiler/types2: types2.h`, `decompiler/util: TypeState`, `game/sound: flava.h`, `decompiler/Function: BlockVtx`, `decompiler/IR2: CondWithElseElement`, `decompiler/level_extractor: ArtData`, `decompiler/util: DataParser.cpp`, `game/graphics: ProfilerNode`, `test/goalc: WithGameTests`, `decompiler/IR2: CaseElement`, `goalc/emitter: ObjectFileData`, `decompiler/data: data/dir_tpages.cpp`, `decompiler/data: LinkedWordReader`, `decompiler/level_extractor: ArtJointAnim`, `goalc/make: .get_additional_dependen`, `goalc/regalloc: AssignmentRange`, `lsp/state: OGGlobalIndex`, `decompiler/analysis: remap_color_move()`, `common/sqlite: GenericResponse`, `decompiler/level_extractor: CompressedFrame`, `common/versions: versions.cpp`, `decompiler/analysis: convert_function_to_atom`, `decompiler/level_extractor: JointAnimCompressedContr`, `goalc/data_compiler: compile_game_text()`, `goalc/regalloc: initialize_unassigned()`, `decompiler/Function: CondNoElse`, `decompiler/ObjectFile: .to_form_script_object()`, `goalc/build_sbk: TailGrowResult`, `goalc/emitter: StaticData`, `goalc/retarget_anim: RetargetOptions`, `goalc/build_sbk: V2GrainEntries`?**
  _High betweenness centrality (0.435) - this node is a cross-community bridge._
- **Why does `BucketId` connect `Renderer Bucket IDs` to `game/graphics: BucketRenderer`?**
  _High betweenness centrality (0.050) - this node is a cross-community bridge._
- **Why does `Merc2` connect `game/graphics: Merc2` to `game/graphics: OpenGLRenderer`, `game/graphics: Merc2.cpp`, `game/graphics: VuLights`, `game/graphics: Merc2BucketRenderer`, `common/custom_data: MercModel`, `game/graphics: Draw`, `Form Expression Analysis`, `game/graphics: Uniforms`, `game/graphics: MercDebugStats`?**
  _High betweenness centrality (0.040) - this node is a cross-community bridge._
- **Are the 19 inferred relationships involving `TypeSpec` (e.g. with `parse_defenum()` and `add_bitfield()`) actually correct?**
  _`TypeSpec` has 19 INFERRED edges - model-reasoned connections that need verification._