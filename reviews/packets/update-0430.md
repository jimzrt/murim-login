<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0430.txt",
      "sha256": "c64926dd865e77de99fde2bd525a808f3dfa6b922976d49f0172dafb846433dd",
      "bytes": 14257
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "75825dca4fbe4063e26cca7c7729fff1899962c546788bec2f0d409d703073cf",
      "bytes": 1689
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "63a23715f5ad9b22a0a45f09af5ba17eb049e72f3afcc18c03f938db719596ab",
      "bytes": 142400
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "ba7119cfa839cbbc46d741e3d1dc49806a535b6bfbdf145d739761da36dad60e",
      "bytes": 803
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "9d02035983e5c37ab8035703970ca02698a5887d28179a0a95c47a3c90757e22",
      "bytes": 824
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "ff7600488f765a62de7b0146ae23ce9423489e38df75f570880cc67691ee8c59",
      "bytes": 667
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "038ab39af644cfe86a1af6321a7219e1ff034eb61021c68c1d35db6c2d959f05",
      "bytes": 1182
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "8b3218a3afda0ec3324c763e1e4567dec657e2d6f1d80c28a668cafdfee44129",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "6021ee098afc0e5a18af27e61be6494734eac666d6823bf8e38ca7dbab2ab5e1",
      "bytes": 132843
    }
  ],
  "estimated_tokens": 10258
}
-->

# Durable State Update — Chapter 430

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 430. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 430. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 430,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 430,
    "continuity_sources": [430],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "Jin Taekyung can perceive the texture of qi and sever layered magic with Force after opening his Middle Dantian.",
    "Magic Johnson has created a near-perfect human appearance for the Skeleton King using magic circles carved into the Skeleton King's bones.",
    "The Skeleton King can now appear human outside his Inventory and is attempting to establish a human-world identity as Stone-King.",
    "Jin recognized a pattern on Magic Johnson's scattered papers as the same pattern he previously saw in Sichuan.",
    "Chairman Shao is preparing a political reckoning against the Crown Prince Party after its persecution and forced labor campaign.",
    "Jin's mother and Hayeon remain in China under Chairman Shao's protection.",
    "Lee Jungryong is publicly presumed dead without a surviving body, while Wu Heixing's corpse was recovered after the battle."
  ],
  "continuity_sources": [
    429,
    428
  ],
  "open_questions": [
    "What do the papers bearing the Sichuan pattern represent, and why did Magic Johnson possess them?",
    "What final punishment will be imposed on Wu Heixing's father and the Crown Prince Party leadership?",
    "How will the Skeleton King's human identity and Stone-King name be formalized in the human world?"
  ],
  "safe_through": 429,
  "temporary_decisions": [
    "Render 샤오 쉔 as “Xiao Shen” and preserve “hyung” for his address to Jin.",
    "Render 매직 존슨 as “Magic Johnson,” 스켈레톤 킹 as “Skeleton King,” and 스톤-킹 as “Stone-King.”",
    "Preserve Jin's dry, profane voice and the Skeleton King's grandiose, Internet-influenced insults."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 이정룡    | **Lee Jungryong** |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 시스템              | **System**                     |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 사천     | **Sichuan**            |
| 귀가      | **your family**                                                 |
| 도사      | **Daoist**                                                      |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 청성파 | **Qingcheng Sect** | Sect named in Baek Museong's comparison about disciplinary rules. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 경호팀장 | **Head of Security** | Go Jun's security-team office under Lee Jungryong. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 쓰촨성 | **Sichuan Province** | Source spelling variant of the established Sichuan location. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 아미파 | **Emei Sect** | Murim sect in Sichuan. |
| 청성 | **Qingcheng** | Short form for Qingcheng Sect. |
| 기문진 | **Mystic Gate Formation** | Formation concealing Dong Feng's clinic in Sichuan. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 쓰촨 | **Sichuan** | Variant spelling used for the region associated with the pattern Jin recognizes. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 마법사 | 이정룡 | Ares Guild mage subordinate to Vice Guild Master | Vice Guild Master | formal-deferential | Lee's five direct A-rank mages greet him and receive instructions for concealing the battle. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 371
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who seeks Jin Taekyung, Cheongpung, and Jeok Cheongang after escaping the confrontation at Mount Song.
- **Personality:** Calm, confident, theatrically frivolous, casually cruel, and ruthlessly destructive; treats allies as disposable tools and enjoys provoking stronger opponents.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He and the Western Heaven Demon Lord serve the same master; he now seeks to personally kill Cheongpung, Jeok Cheongang, and Jin Taekyung, while his former contact Han Su is dead.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 414
- **Aliases:** Team Leader Seok
- **Role:** Leader of Lee Jungryong's security team, an Ares Guild combatant, and Lee's disciple and right-hand man.
- **Personality:** Highly disciplined, fiercely loyal to Lee Jungryong, confident in his abilities, and capable of suppressing his anger and killing intent under provocation.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of Lee Jungryong; leader of Lee's security detail; regarded by Lee as stronger than Park Tae Seop; after Go Jun's defeat by Jin Taekyung, Lee reaffirmed his faith in Go Jun and promised to give him the strength to defeat Taekyung.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 425
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 428
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 412
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃430화



나도 모르게 눈꺼풀이 파르르 떨렸다.

‘……이게 왜 여기에.’

똑똑히 기억하고 있다.

서천마군에 의해 몇 번이나 죽을 위기를 넘겨야 했던 사천혈사(四川血史)가 마무리된 직후, 청성파와 아미파 장문인의 인도하에 향했던 어느 이름 모를 절벽의 동굴.

기문진 뒤에 숨겨져 있던 공간은 실로 광활했고, 그 중심부에는 거대한 진법(陳法)이 새겨져 있었다.

지금 내가 들고 있는 종이에 컬러로 프린트된, 기이한 문양과 기호로 가득한 진법이.

하지만…… 청성과 아미의 장문인들이 이동진(異動陳)이라 이름 붙였던 그것을 더 이상 진법이라고 부를 수 있을까?

나는 다급히 매직 존슨을 향해 종이를 들이밀었다.

“존슨. 이거, 이거 뭐예요?”

「어, 어?」

“이게 왜…… 아니, 도대체 어디서 난 겁니까?”

갑작스러운 내 반응에 당황한 매직 존슨이 얼떨떨한 표정으로 대꾸했다.

「아크 리치가 본거지로 삼았던 도시에서 발견한 마법진이야.」

“마법진이요?”

「응, 마법진. 안 그래도 이것 때문에 한창 연구 중이었는데…… 왜 그래, 진? 혹시 어디서 본 적 있어?」

“다른 것도 있어요?”

「물론이지. 네가 들어오기 전까지 보고 있던 종이들이 전부 그것과 관련된 내용이니까.」

“네?”

그럼 책상 위에 쌓여 있던 그게 전부?

나는 바닥에 널브러진 수십여 장의 종이를 바라보았다.

“자, 잠깐만 실례할게요.”

「진, 진?」

“드디어 미쳐 버린 것인가. 안타깝구나, 못생기고 간악한 인간이여.”

당황한 매직 존슨의 부름과 스켈레톤 킹의 헛소리는 안중에도 없었다.

나는 입을 꾹 다문 채 프린트된 종이 뭉치를 빠르게 훑어 나갔다.

수십 장의 종이에는 각각의 문양과 기호가 새겨져 있었고, 그 모든 것을 다 살펴본 후 한 가지 사실을 깨달을 수 있었다.

‘이건…….’

틀림없다. 배치와 방향이 다를 뿐, 기이한 문양과 기호는 무림에서 본 그것과 동일했다.

그리고 이 종이들을 퍼즐처럼 한데 모으면 하나의 거대한 마법진이 완성된다는 것도.

‘이게 무슨 개 같은 상황이지?’

쇠망치로 뒤통수를 한 대 얻어맞은 기분이다.

말없이 종이들을 노려보던 내가 입을 연 것은 그로부터 상당한 시간이 흐른 뒤였다.

“이거, 아크 리치의 본거지에서 발견한 거라고 하셨죠?”

어느새 시가를 문 매직 존슨을 바라보며 묻자, 그가 연기를 뿜으며 대답했다.

「그래. 나도 처음에는 그런 게 있는 줄 몰랐는데, 조사단 투입 직후에 발견된 것 같아. 이틀째에 연합군을 통해서 전달받았지.」

“전달받았다는 건…….”

「내게 자문을 구했거든. 저쪽에서도 정확히 어떤 기능의 마법진인지 파악하지 못한 거지. 아마 나 말고 다른 두 명에게도 연락이 갔을걸?」

다른 두 명이란 매직 존슨을 제외한 다른 대마도사들일 것이다. 그들이야말로 현존하는 최고의 마법사들이자, 진정한 전문가들이니까.

그리고 그 말은 이 마법진이 지금껏 드러난 적 없는 새로운 종류의 것이라는 뜻이기도 했다.

“그래서, 연구하신 결과는 나왔습니까?”

「아직 정확한 건 아니지만, 마법진의 용도에 대해서는 갈피를 잡았지.」

“용도요?”

「응. 다행히 그쪽에 대해 제법 잘 아는 친구가 하나 있었거든.」

그게 누구냐고 물어보려던 순간, 한 사람이 오만한 목소리로 불쑥 끼어들었다.

“바로 이 몸이시지. 미국 조지아주 애틀랜타에서 출생한 우주 대존잘 미남. 이름하여 스톤-킹.”

맞다. 왜 저놈을 잊고 있었지?

마계 토박이에 네임드 몬스터씩이나 되는 놈이니 뭔가를 알고 있을 것이 분명하다.

나는 헛소리를 늘어놓는 스켈레톤 킹을 다그쳤다.

“개소리하지 말고 아는 거나 빨리 털어놔.”

“앞으로 미스터 킹이라고 부른다면 생각해 보지.”

“미스터 킹 같은 소리 하고 자빠졌네, 낑깡 같은 새끼가.”

“퍽킹 코리안.”

“시벌 놈이.”

“워어, 워어!”

내가 손을 쳐들자 자신도 모르게 후다닥 물러난 스켈레톤 킹이 황급히 외쳤다.

“알았다! 알았다고!”

“말해, 인마.”

경계 어린 눈빛으로 나를 바라본 스켈레톤 킹이 입을 열었다.

“생명력 흡수를 위한 마법진인 것 같다.”

“생명력 흡수?”

“그래. 아크 리치가 다른 인간들의 기운을 흡수하여 힘을 축적하는 용도로 쓴 것 같더군. 그렇게 끌어모은 마력이 있으니 수많은 몬스터 군단을 제어하고 게이트를 열 수 있었던 거겠지.”

중국은 광활한 대륙이다.

대격변으로 엄청난 사상자를 냈음에도 여전히 전 세계 인구의 5분지 1에 해당하는 사람들이 남아 있다.

그리고 그중 쓰촨성에 거주하는 인구는 ‘공식 통계로만’ 약 8천만 명.

이번 몬스터 웨이브가 낳은 사상자는 수백만에 달하고, 아직 공식 집계되지 않은 이들까지 더한다면 실로 어마어마한 숫자로 불어난다.

‘그리고 그들 중 상당수의 목숨이 마력을 위한 희생양이 되었겠지. 놈이 벌였던 짓의 규모를 생각하면 어느 정도 아귀가 맞아떨어져.’

입술을 질끈 깨문 나는 스켈레톤 킹을 향해 재차 물었다.

“확실한 거야?”

“개인적인 유추일 뿐, 장담은 못 한다.”

“어째서?”

스켈레톤 킹이 혀를 찼다.

“간악한 인간이여. 너는 다른 인간들이 사용하는 마법진을 보는 것만으로도 판단할 수 있나?”

“그건…….”

“당연히 모르겠지. 이 몸도 마찬가지다. 주어진 능력에 따라 병사들을 일으켜 세우고 이끌 수는 있어도, 이와 같은 흑마법을 부리지는 못해.”

젠장. 전부 맞는 말이다.

헌터와 몬스터를 각자의 특성에 따라 분류하는 것처럼, 스켈레톤 킹도 딱 그만큼의 능력을 지니고 있을 뿐이다.

기대했던 대답이 나오지 않자 나도 모르게 힘이 빠졌지만, 아직 중요한 질문이 남아 있었다.

“그럼 생명력 흡수 마법진인 건 어떻게 짐작한 거지? 혹시 이런 문양이나 기호들은 몬스터만 알아볼 수 있는 건가?”

스켈레톤 킹이 이 기이한 문양과 기호를 알고 있다면, 녀석에게서 그것들이 의미하는 바를 배울 수 있다면 무림에서 본 진법의 정체도 명확하게 밝혀 낼 수 있다.

기대를 담아 스켈레톤 킹을 바라본 나는, 잠시 후 흘러나온 대답에 맥이 탁 풀렸다.

“저것들이 무엇을 뜻하는지는 모른다. 마법진의 용도는 이 몸이 언데드라 가능했던 일이었고.”

스켈레톤 킹이 매직 존슨을 가리키며 말을 이었다.

“처음 이런 종이로 봤을 때는 잘 몰랐지만, 저 고마운 인간과 함께 현장에 가 보니 확실히 느껴지더군. 나조차도 짐작할 수 없는 수많은 죽음의 냄새가 느껴졌었다. 그때 처음으로 알게 되었지.”

“아…….”

실망감을 감출 수 없었다.

대마도사인 매직 존슨은 물론이고 네임드 몬스터인 스켈레톤 킹조차 알 수 없다면, 당장 저 문양과 기호의 뜻을 알아내는 건 불가능에 가깝다는 뜻이니까.

‘제기랄.’

도대체 무슨 일이 벌어지고 있는 거지?

동굴 중심부에 새겨져 있던 진법, 이번에 발견된 마법진에서 나타난 문양과 기호, 그리고 혈주와 서천마군과의 전투에서 목격한 괴이한 현상들…….

머릿속에 스치는 어떤 불길한 생각을, 마음 깊은 곳에서 애써 부정한다.

그럴 리가 없다고. 있을 수 없는 일이라고.

이건 우연일까. 아니면 운명일까.

운명이라면 난데없이 나타난 이 연결 고리가 의미하는 것은 무엇일까.

한참 동안 말없이 룸 안을 서성이던 나는 불쑥 입을 열었다.

“직접 가 봐야겠어.”

「응?」

“음?”

“존슨. 저 녀석이 가 봤다는 그 현장, 저도 가 볼 수 있죠?”

잠시 고민하던 매직 존슨이 고개를 끄덕였다.

「기밀이긴 하지만…… 진이라면 충분히 가능하지. 단, 모습을 보이는 건 우리 둘뿐이야. 저 친구는 지난번처럼 아공간 포켓에 넣어 가야 해.」

“그럼 됐어요. 바로 출발하시죠.”

「그래, 그러자고. 진도 뭔가 알고 있는 것 같으니.」

나와 매직 존슨이 막 발을 뗀 그때, 스켈레톤 킹이 점잖은 목소리로 끼어들었다.

“듣던 중 미안하지만, 인간들이여. 이 몸은 긴한 용무가 있으니 너희끼리 가 보도록 하거라.”

“……?”

「……?」

“호텔 프런트의 여직원이 매우 아름답더군. 비록 인간의 거죽에 가려져 있지만, 그 안에 숨겨진 골격의 곡선이 끝내줘.”

나는 조용히 되물었다.

“그래서?”

“그래서는 무슨. 오늘은 외박할 것이니 그리 알고 있으라는 이야기지. 그럼 난 이만 미녀와의 약속을 잡으러…… 그런데 간악한 인간이여.”

“왜?”

“갑자기 창을 꺼낸 이유를 물어봐도 되겠나?”

“아, 이거.”

나는 어느새 인벤토리에서 꺼내든 백염을 슬쩍 흔들었다.

“별거 아냐. 네가 돌아서면 찌르려고.”

“음. 그렇군.”

“그렇지.”

“…….”

“왜 안 가? 슬슬 직원들 퇴근할 시간인데. 빨리 가서 저녁 식사라도 하자고 꼬셔야지.”

머뭇거리던 스켈레톤 킹의 입가에 어색한 미소가 맺혔다.

“생각해 보니까 작업은 천천히 걸어도 될 것 같다.”

“우와, 그럼 시간 비겠네. 그럼…….”

나는 환하게 웃으며 사람들에게 인벤토리의 존재를 숨기기 위해 장만한 아공간 포켓 하나를 꺼내 들었다.

“후딱 들어와, 새꺄.”

“……으응.”

시무룩하게 대답한 스켈레톤 킹이 아공간 포켓 안으로 모습을 쏙 감췄다.



* * *



마법진을 직접 눈으로 본 순간, 나는 스켈레톤 킹이 했던 말의 의미를 깨달을 수 있었다.

아니, 어쩌면 녀석의 말을 들은 직후라 더 그렇게 느꼈는지도 모르겠다.

하지만 보는 것과 동시에 압도되었고, 나도 모르게 한 가지 단어를 떠올렸다.

‘죽음.’

동굴에서 봤던 것과는 비교도 안 될 만큼 거대한 크기의 흑마법진.

비록 마력이 끊기고 본래의 기능을 잃었다고는 하나, 한때 숱한 생명을 뺏었던 죽음의 흔적마저 사라지지는 않았다.

그리고…… 그것이 내가 느낀 전부였다.

「진. 어때? 뭔가 알 것 같아?」

“아뇨. 전혀.”

알 수 없는 순서, 배치로 이루어진 문양과 기호는 여전히 해석이 불가능했다.

앞서 무림에서 그랬던 것처럼 시스템은 잠잠했고, 아무런 소득도 얻지 못한 나는 몇 시간이나 근처를 서성거리다가 발길을 돌릴 수밖에 없었다.

“미스터 존슨, 그리고 진. 돌아가시는 길에 불편함이 없도록 경호를 준비했는데…….”

“괜찮습니다.”

“예. 그럼 모쪼록 다음에 뵙기를.”

우리는 칼 같은 각도로 거수경례를 올린 보안 책임자와 경비대를 뒤로하고 걸음을 옮겼다.

주위에 아무도 없음을 확인한 매직 존슨이 작게 입술을 달싹였다.

「진. 뭔가 알고 있는 것 아니었어?」

“……꿈. 꿈속에서 비슷한 걸 봤나 봐요.”

「흠.」

“존슨. 저 잠시만 혼자 주위를 둘러봐도 될까요?”

「물론이지. 얼마나 걸릴 것 같아?」

“금방 돌아올게요.”

나는 천천히 폐허를 거닐기 시작했다.

자정이 넘은 깊은 밤이었음에도 도시는 정오처럼 환했고, 수많은 사람과 기계가 폐허가 된 도시를 수습하고 있었다.

아마 지금쯤 전쟁에 휘말린 도시 곳곳에서 이와 같은 작업이 벌어지고 있을 것이다.

‘사천에서도 마찬가지겠지.’

쓰촨과 사천은 전혀 다른 세상으로 나뉘어 있다. 무림은 현대의 과거가 아니며, 현대는 무림의 미래가 아니다.

하지만 이처럼 완전히 다른 두 세상을 잇는 연결 고리가 나타났고, 이는 처음 있는 일이 아니었다.

‘캡슐.’

나를 둘러싼 모든 것은 분리수거장에서 주웠던 고물 캡슐로부터 시작되었다.

어떻게, 왜, 무슨 이유로?

걸음을 옮길 때마다 떠오르는 의문들로 머릿속이 엉망이다.

“후우.”

내 깊은 한숨에, 아공간 포켓에서 슬쩍 인벤토리로 옮겨 놓은 스켈레톤 킹이 물었다.

- 괜찮나, 간악한 인간?

“지금 걱정해 주는 거냐?”

- 아니. 괜찮으면 빨리 호텔로 돌아가자고. 며칠 전에 존슨한테 들었는데 근처에 물 좋은 클럽이 있다더군.

“…….”

내 감동 돌려 내, 미친놈아.

나는 존슨이 말한 물 좋은 클럽의 정체가 게이 바라는 걸 말해 줄까 하다가 참았다.

“됐다. 내가 너한테 뭘 바라냐.”

- 그래서, 언제 돌아가는 건가?

“간다, 이 새끼야. 간다고!”

빡침을 이기지 못하고 소리친 바로 그 순간이었다.

“어딜 그렇게 가고 싶은 건가. 지옥?”

어느 때보다 딱딱하고 냉기가 흐르는 목소리에, 나는 천천히 돌아섰다.

나도 모르는 사이에 깊숙한 곳으로 들어왔는지 비교적 어두운 폐허 너머, 익숙한 얼굴이 무너진 건물을 헤치며 걸어오고 있었다.

“지옥은 너희 영감님이 가신 곳이고, 만약 내가 죽는다면 천국이지.”

이정룡의 제자이자 경호팀장, 석고준의 눈이 차갑게 가라앉았다.
```

## Final English reading copy

```markdown
# Chapter 430

My eyelids began to tremble before I even realized it.

*Why is this here…?*

I remembered it clearly.

Immediately after the Sichuan Blood History—after the Western Heaven Demon Lord had nearly killed me several times—I had followed the Sect Leaders of the Qingcheng and Emei Sects to a cave in an unnamed cliff.

The space hidden behind the Mystic Gate Formation had been truly vast, and a gigantic formation had been carved into its center.

A formation filled with strange patterns and symbols, printed in color on the paper I was holding now.

But… could that thing, which the Sect Leaders of Qingcheng and Emei had named the Moving Formation, still be called a formation?

I hurriedly shoved the paper toward Magic Johnson.

“Johnson. This—what is this?”

「Huh? What?」

“Why is this here…? No, where did you get it?”

Taken aback by my sudden reaction, Magic Johnson answered with a bewildered expression.

「It’s a magic circle discovered in the city the Arch Lich used as its base.」

“A magic circle?”

「Yes, a magic circle. I was already in the middle of researching it because of this… Why? Jin, have you seen it somewhere before?」

“Are there more?”

「Of course. Every sheet of paper I was looking at before you came in is related to it.」

“What?”

Then everything piled up on the desk was related to it?

I looked at the several dozen sheets of paper scattered across the floor.

“Excuse me for a moment.”

「Jin? Jin?」

“Has he finally gone mad? How tragic, you vile and ugly human.”

I paid no attention to Magic Johnson’s flustered calls or the Skeleton King’s nonsense.

With my mouth pressed tightly shut, I rapidly skimmed through the stack of printed papers.

Each sheet contained its own patterns and symbols. After examining all of them, I realized one thing.

*This is…*

There was no mistake. The strange patterns and symbols were identical to the ones I had seen in Murim. Their arrangement and orientation were merely different.

And if I assembled all these papers together like pieces of a puzzle, they would form one enormous magic circle.

*What the hell kind of situation is this?*

It felt as if someone had struck the back of my head with a sledgehammer.

I stared silently at the papers for a long time before finally opening my mouth.

“You said this was discovered at the Arch Lich’s base, right?”

Magic Johnson had a cigar between his lips by then. When I looked at him and asked, he exhaled smoke before answering.

「That’s right. I didn’t even know something like this existed at first, but it seems to have been discovered soon after the investigation team was deployed. I received it through the coalition forces on the second day.」

“You received it?”

「They asked for my advice. They couldn’t figure out exactly what kind of function the magic circle had, either. They probably contacted the other two as well.」

The other two were probably the Grand Mages besides Magic Johnson. They were the greatest mages alive and true experts in the field.

And that meant this magic circle was a new kind that had never been revealed before.

“So, did you figure anything out through your research?”

「Not precisely yet, but I’ve gotten a general idea of the magic circle’s purpose.」

“Its purpose?”

「Yes. Fortunately, I have a friend who knows quite a bit about that sort of thing.」

I was just about to ask who he meant when someone suddenly interrupted in an arrogant voice.

“That would be this very body. The universe’s most insanely handsome man, born in Atlanta, Georgia, United States. Known as Stone-King.”

That was right. Why had I forgotten about this bastard?

He was a native of the Demon Realm and a Named Monster, so he was bound to know something.

I pressed the Skeleton King, who was spouting nonsense.

“Quit talking bullshit and tell me what you know.”

“Call me Mr. King from now on, and I shall consider it.”

“Mr. King, my ass. You kumquat-looking bastard.”

“Fucking Korean.”

“You son of a bitch.”

“Whoa, whoa!”

When I raised my hand, the Skeleton King instinctively scurried backward and shouted in alarm.

“All right! I said all right!”

“Talk, you bastard.”

The Skeleton King regarded me warily before opening his mouth.

“It appears to be a magic circle for absorbing life force.”

“Absorbing life force?”

“That is correct. It seems the Arch Lich used it to absorb the energy of other humans and accumulate power. With all that mana gathered, it was able to control countless monster legions and open Gates.”

China was a vast continent.

Even after suffering enormous casualties during the Great Cataclysm, it still had a population equivalent to one-fifth of the world’s total.

And the population living in Sichuan Province alone was approximately eighty million—according to official statistics, at least.

The monster wave had caused casualties numbering in the millions. If the people who had yet to be officially counted were included, the number would swell to something truly enormous.

*And a considerable number of those people must have been sacrificed to provide mana. Considering the scale of what that bastard had done, it all adds up.*

I bit down hard on my lip and asked the Skeleton King again.

“Are you sure?”

“That is merely my personal inference. I cannot guarantee it.”

“Why not?”

The Skeleton King clicked his tongue.

“Vile human. Can you determine the meaning of magic circles used by other humans simply by looking at them?”

“That’s…”

“Of course you cannot. This body is no different. I can raise and command soldiers according to the abilities granted to me, but I cannot wield dark magic like this.”

Damn it. He was completely right.

Just as Hunters and monsters were classified according to their individual traits, the Skeleton King possessed only that much ability.

His answer wasn’t what I had hoped for, and I could not help feeling deflated. But one important question remained.

“Then how did you guess that it was a life-force absorption magic circle? Can only monsters recognize patterns and symbols like these?”

If the Skeleton King knew these strange patterns and symbols, and if I could learn what they meant from him, I might finally be able to identify the formation I had seen in Murim.

I looked at the Skeleton King expectantly, but the answer that emerged a moment later left me utterly deflated.

“I do not know what those things mean. I could guess what the magic circle was for only because I’m undead.”

The Skeleton King pointed at Magic Johnson and continued.

“When I first saw something like this on paper, I did not know what it was. But when I visited the site with that human I’m grateful to, I could sense it clearly. I could smell countless deaths—more than even I could guess at. That was when I first realized it.”

“Oh…”

I could not hide my disappointment.

If even Magic Johnson, a Grand Mage, and the Skeleton King, a Named Monster, could not understand them, then figuring out the meaning of those patterns and symbols right away was practically impossible.

*Damn it.*

What on earth was happening?

The formation carved into the center of the cave. The patterns and symbols that had appeared in the magic circle discovered this time. The bizarre phenomena I had witnessed during my battle with the Blood Lord and the Western Heaven Demon Lord…

I desperately denied the ominous thought that flashed through my mind.

*That can’t be. It’s impossible.*

Was this a coincidence? Or was it fate?

And if it was fate, what did this connection that had appeared out of nowhere mean?

After pacing silently around the suite for a long time, I suddenly spoke.

“I need to see it in person.”

「Huh?」

“Hmm?”

“Johnson. I can visit the site that bastard went to, right?”

Magic Johnson thought for a moment before nodding.

「It’s classified, but you should be allowed to go, Jin. However, only the two of us can show ourselves. We’ll have to take that friend in an extradimensional pocket, like last time.」

“That’s good enough. Let’s leave right away.”

「All right, let’s do that. It seems Jin knows something, too.」

Just as Magic Johnson and I were about to set off, the Skeleton King interrupted in a dignified voice.

“I apologize for interrupting, humans, but this body has pressing business. You two may go without me.”

“……?”

「……?」

“The female employee at the hotel front desk is exceptionally beautiful. Though covered in human skin, the curves of the skeleton beneath it are exquisite.”

I quietly asked,

“So?”

“What do you mean, ‘so’? I am informing you that I shall be spending the night out today. You should keep that in mind. Now, I must go arrange a date with the beauty… But, vile human.”

“What?”

“May I ask why you suddenly took out a spear?”

“Ah, this?”

I casually waved White Flame, which I had somehow already pulled from my Inventory.

“It’s nothing. I was going to stab you when you turned around.”

“I see.”

“Exactly.”

“……”

“Why aren’t you leaving? The employees will be getting off work soon. You should hurry and persuade her to have dinner with you.”

The Skeleton King hesitated, and an awkward smile formed around his mouth.

“Come to think of it, I suppose I can take my time making a move on her.”

“Wow, then you’ve got some free time. In that case…”

I smiled brightly and pulled out one of the extradimensional pockets I had acquired to conceal the existence of my Inventory from other people.

“Get in there, asshole.”

“……Uh-huh.”

The Skeleton King answered dejectedly and slipped inside the extradimensional pocket.

* * *

The moment I saw the magic circle with my own eyes, I understood what the Skeleton King had meant.

Or perhaps it only seemed that way because I had heard his explanation immediately beforehand.

Regardless, the sight overwhelmed me, and one word surfaced in my mind before I could stop it.

*Death.*

It was a dark magic circle so enormous that the one I had seen in the cave could not even compare.

Although its mana had been cut off and it had lost its original function, even the traces of death left behind by the countless lives it had once claimed had not disappeared.

And… that was all I could feel.

「Jin. What do you think? Do you have any idea what it is?」

“No. Not at all.”

The patterns and symbols, arranged in an incomprehensible sequence, were still impossible to decipher.

Just as it had in Murim, the System remained silent. After wandering around the area for several hours without gaining anything, I had no choice but to turn back.

“Mr. Johnson, and Jin. We prepared an escort so you won’t encounter any inconvenience on your way back…”

“We’re fine.”

“Yes. Then I hope to see you again next time.”

We left the security chief and his guards behind. They had given us a salute at an angle sharp as a knife.

After confirming that no one was nearby, Magic Johnson quietly moved his lips.

「Jin. You knew something, didn’t you?」

“…A dream. I think I saw something similar in a dream.”

「Hmm.」

“Johnson. Can I look around by myself for a moment?”

「Of course. How long do you think it’ll take?」

“I’ll be back soon.”

I began walking slowly through the ruins.

Although it was well past midnight, the city was as bright as noon, and countless people and machines were working to clear away the ruins.

Similar work was probably underway throughout the cities caught up in the war.

*Sichuan would be the same.*

China’s Sichuan and Murim’s Sichuan were completely different worlds. Murim was not the modern world’s past, and the modern world was not Murim’s future.

But a connection linking those utterly different worlds had appeared—and this was not the first time.

*The capsule.*

Everything surrounding me had begun with the junk capsule I had picked up at a recycling center.

*How? Why? For what reason?*

Each step brought new questions to mind, leaving my thoughts in complete disarray.

“Phew.”

At my deep sigh, the Skeleton King—who had been moved from the extradimensional pocket into my Inventory—asked,

“Are you all right, vile human?”

“Are you worried about me now?”

“No. If you are all right, let us return to the hotel quickly. Johnson told me a few days ago that there’s a club nearby with a great crowd.”

“……”

*Give me back my touching moment, you lunatic.*

I considered telling him that the club Johnson had mentioned was a gay bar, but held my tongue.

“Forget it. What do I expect from you?”

“When are we returning?”

“I’m going, you bastard. I said I’m going!”

It happened at that exact moment.

“Where are you in such a hurry to go? Hell?”

At the sound of the voice—harder and colder than ever before—I slowly turned around.

Without realizing it, I must have ventured deep into the ruins. Beyond the relatively dark ruins, a familiar figure was making his way through a collapsed building toward me.

“Hell is where your old man went. If I die, I’ll go to heaven.”

The eyes of Go Jun—the Disciple of Lee Jungryong and Head of Security—settled into a cold, icy stare.
```
