<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0460.txt",
      "sha256": "05ce3de190ebeb62ce103749f5ba7ff92d3ae27a9f31fe67bead82d011e2b51a",
      "bytes": 13286
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "657f19ff4c4de04291baa9fad7a6b1f9a99fb2e219c89b5b032001413ee8340a",
      "bytes": 3847
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b35c66ac467942d7455c2e1c86c144e770be21626f3edc06722702ab7cf5afb5",
      "bytes": 150026
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "50c3dcaf7edeb003c98cd52a99b0bcfad3d3ce4766de8645a4ff1a31fec04e8b",
      "bytes": 990
    },
    {
      "path": "characters/Dongting Fisherman.md",
      "sha256": "a17d3bc3444cd384f80ec5ad02706f87e14be04f2423d9429380a3310e74c8a5",
      "bytes": 703
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "a976c5baf744fd5183160af496ae8df60a3a2b01f013e7dfda816c5b0fa20589",
      "bytes": 662
    },
    {
      "path": "characters/Honglan.md",
      "sha256": "44f64524fc554444a88c1da44fbebd1e94c805b9cfb4750fd5b9bfdb745a2d61",
      "bytes": 751
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "983d856d2153555582e433cc72f2f21f9a8ffd73840764deb3f898449863ec7c",
      "bytes": 667
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "1df3b26810ce6ddf4b2bef2980797cf89e1af2db38a0da178cb8085aad74fee7",
      "bytes": 1108
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8c50b16ddd4db47c125932b0035ad17123317334a365f0c8daedd7279da91ecf",
      "bytes": 145189
    }
  ],
  "estimated_tokens": 10476
}
-->

# Durable State Update — Chapter 460

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 460. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 460. Profile updates may replace only one
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
  "chapter": 460,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 460,
    "continuity_sources": [460],
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
    "Taekyung completed the unavoidable Peak-grade Quest The Tragedy of Dongting Lake, rescued two people who were the only survivors found, and earned the Water Rescue Worker Title.",
    "Honglan survived the Dongting Lake disaster and regained consciousness; Ju Wongong also survived but remains unconscious under guard after passing the most dangerous stage of his injuries.",
    "Jin Wikyung is acting as an inspector for the new Murim Alliance and is cooperating with Taekyung's investigation.",
    "The shared symbols between the Arch Lich's magic circle and Dark Heaven's formations remain unexplained.",
    "The Sea Serpent Society and three Yangtze River Channel League strongholds, including Donghu Stronghold, were destroyed, with more than a thousand casualties, while the perpetrators' wider plans remain unknown.",
    "The Dongting Fisherman is a previous-generation Supreme Peak water-arts master comparable to the Seafaring King, remains in Hubei Province, and is suspected of being Dark Heaven's operative and the perpetrator of the Dongting Lake attack.",
    "Wudang is responding to an unidentified killer demon responsible for more than thirty deaths, including twenty pilgrims on Mount Wudang.",
    "The Skeleton King's undead identity remains concealed, and Taekyung has ordered him to join Peace Guild under a prepared contract.",
    "Go Jun is expected to succeed Lee Jungryong as Ares Guild's captain and is searching China for Lee's holographic recorder.",
    "The captured Three Fiends is a former-generation great fiend and Supreme Peak Dark Heaven subordinate whom Taekyung is transporting alive to investigate possible codes or markings.",
    "Qingxia Hall is an influential Hubei social club formed by powerful families' children, and Ju Wongong is its exiled young master who defers to Prince Shangshan while Honglan conceals her real name.",
    "Beggars' Sect, Lower District Sect, and Zhuge Clan intelligence are searching for the people responsible for the Hubei massacres."
  ],
  "continuity_sources": [
    459,
    458
  ],
  "open_questions": [
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Who destroyed Donghu Stronghold and the related Yangtze River Channel League strongholds, why was no Moving Formation trace left, and was the destruction a diversion?",
    "What is the Dongting Fisherman's exact role in Dark Heaven and the Hubei atrocities, and what do his hidden refuges contain?",
    "Is the killer demon attacking Wudang connected to Dark Heaven?",
    "What evidence is contained in Lee Jungryong's holographic recorder, and what are the terms of the Peace Guild–Wizard Guild agreement?"
  ],
  "safe_through": 459,
  "temporary_decisions": [
    "Render 익양루 as Yiyang Tower.",
    "Render 황철 as Hwang Cheol, 도립군 as Do Ripgun, 광수도귀 as Mad Water Saber Demon, 파랑호 as Wave Fox, 동정호 as Dongting Lake, and 사천혈사 as Sichuan Blood Tragedy.",
    "Render 살귀 as killer demon, 일급 낭인 as First Rate wandering martial artist, 삼괴 as Three Fiends, 대마두 as great fiend, and 마군 as Demon Lord.",
    "Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”",
    "Preserve the Skeleton King's grandiose, mock-offended voice and Taekyung's dry, profane humor; render 주원공 as Ju Wongong, 대죽산표국 as Daejuksan Escort Bureau, 형문검가 as Hyungmun Sword Family, 응성상회 as Eungseong Merchant Association, 천룡인 as Celestial Dragon, 사인교 as four-person sedan chair, 홍란 as Honglan, 가기 as singing courtesan, 구족 as the nine branches of kin, 수상 구조대원 as Water Rescue Worker, and 수공 as water arts."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 은인     | **Benefactor**                               |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 소저      | **Young Lady**                                                  |
| 동정어옹 | **Dongting Fisherman** | Publicly condemned the Yangtze River Channel League and disappeared three days before this chapter. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 홍란 | **Honglan** | Stage name of Ju Wongong's Lower District Sect singing courtesan; her real name is concealed. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 후개 | **Successor Beggar** | Title of the Beggars' Sect successor competing in the preliminaries. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 홍란 | 은인 | rescued_survivor_to_rescuer | Benefactor | humble-formal | Honglan addresses Taekyung as Benefactor after he rescued her. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 458
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Dongting Fisherman.md

# Dongting Fisherman (동정어옹)

- **Safe through:** Chapter 459
- **Aliases:** None
- **Role:** The Dongting Fisherman is a previous-generation Supreme Peak master whose water arts rival the Seafaring King; he is identified as Dark Heaven's tail and suspected perpetrator of the Dongting Lake attack, with hidden refuges throughout the lake.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** The Dongting Fisherman opposed the Yangtze River Channel League and was monitored by the Lower District Sect for several years after friction with it, while current records place him in Hubei Province.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 459
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung and uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and search for Dark Heaven’s Hubei forces.

### Honglan.md

# Honglan (홍란)

- **Safe through:** Chapter 459
- **Aliases:** None
- **Role:** Honglan is a Lower District Sect courtesan who uses a stage name while serving as Ju Wongong's singing courtesan.
- **Personality:** Discreet about her real identity and professionally alluring.
- **Voice:** Clear, pure, and alluring, with humble formal speech toward honored guests.
- **Relationships:** Honglan is kept at Ju Wongong's side as a singing courtesan, belongs to the Lower District Sect, can respond to Taekyung through Sound Transmission, and is the sole surviving eyewitness to the Dongting Lake attack who knows several possible locations of the Dongting Fisherman's hidden refuges.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 448
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 459
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

## Korean source

```text
＃460화



여러모로 좋지 않은 날씨였다.

지난 밤사이 수십 척의 선박과 생명을 집어삼킨 동정호의 강물은 거칠었고, 저 멀리서부터 불어오는 바람은 난폭했다.

그리고 이런 기상 상황에서 배를 띄우는 것은 동정호를 제 손바닥 보듯 들여다본다는 늙은 사공의 생각으로도 과히 좋지 않은 선택이었나 보다.

“쇠, 쇤네는 못 하겠습니다요.”

그것이 처음부터 억지로 끌려온 기색이 역력했던 사공의 첫마디였다. 그는 초조한 얼굴로 말을 이었다.

“귀인들께서 가고자 하시는 곳들은 동정호에서도 유난히 폭이 좁고 물살이 거친 곳인데……. 하물며 이런 날씨라면 더더욱 무립니다요.”

“그러니 사공께 청하는 것입니다. 상선이나 군선으로는 진입할 수 없어도, 동정호에서 가장 솜씨 좋은 사공이 모는 튼튼한 나룻배라면 가능할 테니까요.”

“아무리 그리 말씀하셔도…….”

“사공?”

“예, 예?”

“부탁드릴게요.”

남자는 아무리 나이가 들어도 남자다.

홍란의 조곤조곤한 목소리와 눈부신 미모에 넋이 나간 늙은 사공은 나룻배에 오른 뒤에야 비로소 정신을 차렸다.

“내가 미쳤지, 미쳤어. 지난밤에 그 사달이 난 걸 알면서도 배를 띄우다니. 은영귀(隱影鬼)라도 만나는 날에는 어찌하려고…….”

은영귀?

귓가를 파고드는 푸념에 낯선 단어가 섞여 있다. 고개를 돌리자, 겁에 질린 사공과 눈이 마주쳤다.

그는 침을 꿀꺽 삼키고서야 대답했다.

“말 그대로 귀신 같은 놈입지요. 근래 들어 그놈에게 당한 사공들이 수두룩합니다요. 쇤네와 오래 알고 지낸 녀석도 밤에 몇 푼 더 벌어 보겠다고 나갔다가 그만…….”

늙은 사공은 짙은 두려움이 배인 눈동자로 동정호의 출렁이는 강물을 응시했다.

“여하간 그림자도 못 보고 죽는다고 해서 은영귀라 불립니다. 이건 쇤네의 하찮은 소견인데, 요즘 벌어지는 일들도 놈의 짓이 분명합니다요. 전부 그 악귀의 소행인 게지요.”

궁기방이 혀를 차며 끼어들었다.

“악귀는 무슨. 이보시오, 사공. 내가 지금껏 그런 이야기를 한두 번 들은 줄 아시오? 만약 그 말들이 전부 사실이었으면 천하의 물고기 중 절반은 인면어(人面魚)고, 산에는 천 년 묵은 백호와 용들이 득실거릴 거요.”

“이건 한 치의 거짓도 없는 사실입니다. 천인공노할 일이 계속되니 동정호의 신령께서 노하신 것이 틀림없어요.”

“악귀도 모자라서 신령까지? 됐소. 말을 맙시다.”

“아니, 호북성 뱃사람이면 누구나 다 들어 본 얘긴데…….”

“내가 뱃사람으로 보이시오?”

“그건 아닙니다요. 누가 봐도 거지 중의 상거지 아닙니까.”

“아, 맞는 말이긴 한데 갑자기 열 받네.”

“고, 고정하십시오. 귀인. 이 늙은이는 그저 들은 그대로 아뢴 죄밖에 없습니다.”

늙은 사공의 목소리에는 억울함이 가득했다.

온갖 설화와 미신이 사실처럼 여겨지는 무림에서 일평생 뱃사람으로 살아온 그다.

그래서인지 사공은 최근 잇따라 벌어진 흉흉한 사건이 은영귀라 칭한 악귀의 소행이라 철석같이 믿는 듯했다.

‘생각해 보면 아주 헛소리도 아니지.’

홍란과 청풍의 표정을 보니 그들도 나와 같은 생각을 떠올린 모양이었다.

시선이 마주치기 무섭게 두 사람이 동시에 입을 열었다.

“은인, 혹시…….”

“은인, 저 사공이 말하는 은영귀가…….”

“잠깐. 둘 다 무슨 말을 하고 싶은지는 알겠으니까 굳이 말 안 해도 돼요. 그리고 곧 죽어도 은인이라고 하고 싶으면 차례차례 말해. 헷갈려.”

하나로도 벅찬 은인 무새가 더 늘었네.

가끔 이럴 때마다 내가 대단한 사람이 된 것 같다.

아니, 그런데 홍란은 목숨을 구해 줬으니 그렇다 쳐도, 청풍 저 인간은 배고플 때 당과 몇 개 줬다고 평생 은인으로 모실 생각인가.

한숨을 내쉰 내가 말을 이었다.

“그래, 아마도 은영귀는 동정어옹일 확률이 높겠지. 아니면 혼란한 틈을 타 노략질을 벌이는 놈들이거나.”

“맞아요, 제가 말하려던 게 그거였어요. 은인.”

청풍에 질세라 홍란 역시 고개를 끄덕인다.

“천녀도 그리 생각합니다. 은인.”

“아니, 한 사람씩만 말하라니까.”

어찌 되었건 간에 단순한 자연적 사고일 확률은 희박했다.

지금까지 말을 들어 보니 죽은 사공이 한둘이 아닌 데다가, 다음 순간 이어진 늙은 사공의 말 또한 신빙성을 더해 주었다.

“그러고 보니 죽은 사공들이 사라진 지점이 전부 엇비슷합니다. 어? 잠깐, 귀인들께서 가려고 하시는 곳도 그 주변인데…….”

순간 멈칫한 늙은 사공이 천천히 고개를 들었다.

말없이 우리를 차례차례 훑어본 그가, 출발을 위해 잡고 있던 노를 슬그머니 내려놓고 일어났다.

“어디 가십니까?”

내 물음에 늙은 사공이 어색하게 웃었다.

“그게, 소피를 보는 걸 깜빡했지 뭡니까요.”

“무진아.”

“예, 조장님.”

“사공께서 소피가 마려우시단다.”

“그렇습니까?”

이제는 척하면 척이다.

자신에 비하면 거인이나 다름없는 혁무진이 막아서자, 늙은 사공의 눈동자가 도살장에 끌려가는 송아지처럼 촉촉해졌다.

“지금도 마려우시오?”

혁무진의 낮은 목소리에 사공이 고개를 저었다.

“……생각해 보니 마렵지 않습니다.”

“잘됐구려. 우려하는 일이 벌어지기 전에 보내 줄 테니 너무 걱정하진 마시오.”

나이 든 사공에게 못 할 짓을 하는 것 같아 미안하긴 하지만, 동정어옹의 거처로 가기 위해서는 능숙한 길잡이의 역할이 필수였다.

우리가 가고자 하는 곳은 나룻배 몇 척 정도만 드나들 수 있는 좁은 길.

관부가 백 척의 함대와 수만의 관군들을 동원한다 해도 진입할 수 없을뿐더러, 되려 무거운 짐 덩어리에 불과하다.

‘만약 동정어옹과 전투가 벌어진다면 희생만 늘어날 뿐이야.’

관부는 도주를 대비하여 동정호와 장강으로 이어지는 길목을 빈틈없이 봉쇄하고, 나와 청풍을 포함한 소수 정예가 동정어옹을 추격하여 생포 혹은 척살하는 것이 최선이었다.

그리고 동정어옹의 처리만큼이나 중요한 것은, 더 이상의 헛된 희생이 없어야 한다는 것이다.

생각을 끝마친 나는 불쑥 입을 열었다.

“혁무진, 궁기방, 홍 소저. 세 사람은…….”

“싫습니다.”

“어디서 개가 짖나.”

“저도 미력한 힘이나마 보태겠어요.”

말이 끝나기도 전에 튀어나오는 대답에 말문이 턱 막힌다. 그런 내 모습에 혁무진과 궁기방이 혀를 끌끌 찼다.

“뻔합니다. 뻔해요.”

“무슨 말 하려는지 훤히 보인다.”

“여기까지 와서 어떻게 돌아갑니까. 명색이 사내대장부가.”

“나도 마찬가지다. 대 개방의 후개가 고작 이 정도로 겁을 먹을 수는 없지.”

“조장님께서는 뭐 좀 위험할 것 같으면 무조건 빠지라고 하시더라. 하여간 이 정도면 조장님 특징이에요. 조특.”

“의외로 새가슴이라니까.”

“그런데 궁 소협은 아까부터 왜 자꾸 제 말을 따라 하십니까? 거 되게 신경 쓰이게.”

“이 빌어먹을 놈이 왜 잘 나가다가 시비를 걸지? 간이 배 밖으로 나왔냐?”

“거지 특. 객잔에서 버리는 음식으로도 부족해서 남의 말도 주워 먹음.”

“……아니, 이런 개만도 못한 놈을 봤나.”

“어쨌건 저는 조장님이 뭐라 하셔도 따라갑니다. 어릴 때 용한 점쟁이가 제 사주를 봤는데, 백 살 넘어서까지 부귀영화를 누리며 잘 먹고 잘 산다고 했습니다. 오늘 죽을 리가 없어요.”

호언장담하는 혁무진의 모습을 어이없이 바라보던 궁기방이 고개를 저었다.

“후우, 됐다. 말을 말아야지. 그리고 나도 혁가 놈과 같은 생각이니 떼 놓고 갈 생각은 추호도 하지 마라. 나 역시 개방의 절기를 이어받은 몸. 너나 청 소협만큼은 아니더라도 이 한목숨 건사하는 데는 아무런 문제 없어.”

“…….”

나는 말을 꺼내지 못하고 입술만 달싹거렸다.

사실 따지고 보면 두 사람 모두 어디 가서 무시당할 수준은 아니었다.

혁무진은 비교적 늦게 무공을 익히기 시작했음에도 나와 함께 위기를 넘나들며 폭발적으로 성장했고, 궁기방은 후개가 될 만큼 뛰어난 자질의 소유자이자 원숙한 경지에 접어든 절정 고수니까.

‘하지만 두렵다.’

가까운 사람을 잃는다는 것이. 다시 한번 그날의 과거가 반복될 것 같아서 두렵다.

내가 망설이던 그때, 청풍이 문득 입을 열었다.

“은인. 저도 은인이 간다면 지옥 끝까지 따라갈 수 있어요.”

“청 소협.”

“안 된다고 하지 마세요. 저도 당당한 사내이고 무인인걸요.”

“청 소협.”

청풍이 살짝 웃으며 고개를 저었다.

“은인. 아무 말씀도 하지 마세요. 제가 은인을 믿는 만큼, 은인도 우리를 믿어 주시면 돼요.”

“아니, 그게 아니라 당신은 무조건 함께 가는 건데 왜 굳이 나서서…….”

“앗. 아아…….”

“괜한 소리 하지 말고 앉아 있어. 분위기 깨지 말고.”

“……예. 은인.”

시무룩해진 녀석의 모습에 피식 실소가 터져 나왔다. 나는 혁무진과 궁기방을 향해 고개를 끄덕였다.

“하나만 명심해. 어떤 상황에서도 내 판단에 따를 것. 그것이 설령 나를 버리고 도망치라는 명령이라고 해도.”

“조장님. 그건…….”

머뭇거리는 혁무진의 옆구리를 궁기방이 슬쩍 찔렀다.

“그럼, 명심하고말고. 혁가 놈도 마찬가지일 거다. 그렇지?”

“예? 아, 예.”

속이 뻔히 들여다보이는 상황이었지만 모르는 척 넘어갔다.

나는 그런 상황이 오지 않도록 최선을 다할 것이고, 녀석들이 위험에 빠지기 전에 떼어 놓을 자신이 있었다.

하지만, 마지막 남은 한 사람은 곤란하다.

“제가 무슨 말을 하려는지, 이미 알고 계실 겁니다. 그렇죠?”

홍란의 붉은 입술이 스르륵 열렸다.

“정확한 길을 알려 줄 사람이 필요할 거예요.”

“괜찮습니다. 홍 소저의 말대로라면 동정호에서 가장 뛰어난 사공이 함께하고 있으니까요.

“만약 예상치 못한 변수가 생기면요?”

“잘 대처할 겁니다.”

“비록 은인과 다른 분들께 비하면 초라하지만, 저 역시 일류의 경지에 오른…….”

“알고 있습니다. 그리고 그 일류 고수가 몇 시진이 넘도록 건장한 사내를 붙잡은 채 강물에 잠겨 있다가, 정신을 차린 지 반 시진밖에 되지 않았다는 사실도.”

“……!”

정곡을 찔린 홍란이 지그시 입술을 깨물었다.

누구보다 그녀 스스로가 잘 알고 있을 것이다.

지금처럼 거동할 수 있는 것과 치열한 전투를 치른다는 건 전혀 다른 문제라는 것을.

“이번에도 지켜볼 수밖에 없겠군요. 저는.”

“이번에도?”

“네. 오래전의 그때도, 지난밤에도. 그리고 지금도.”

내 눈에 담긴 의문을 읽어 낸 홍란이 미소지었다. 지금까지 봐 왔던 어떤 것보다 씁쓸한 웃음이었다.

“하루아침에 가문과 부모를 잃은 여아가 지금의 모습으로 있기까지는…… 참으로 많은 일이 있었지요.”

“아.”

“잠시만 실례할게요.”

반짝이는 눈동자로 나를 올려다보던 그녀가 나직한 목소리와 함께 손을 뻗는다.

희고 가느다란 손가락이 헝클어진 머리카락과 목을 스치자, 나도 모르게 몸이 움찔 떨렸다.

“홍 소저, 이게 무슨…….”

“다 됐어요. 아, 훨씬 낫다. 한 번 보실래요?”

홍란의 손가락을 따라 시선을 내리자, 동정호의 맑은 강물에 누군가의 모습이 비친다.

말끔하게 정돈된 머리카락과 그것을 고정한 아름다운 은비녀 하나.

고개를 들자 말갛게 웃고 있는 홍란의 얼굴이 눈에 들어온다.

“은인, 아니 진 대협(大俠).”

어느새 풀어 헤쳐진 그녀의 머리카락이 바람을 타고 부드럽게 흔들렸다. 출렁대고, 찰랑거리다가 어느새 찬란해진다.

“무운을 빌어요.”

나직한 목소리가 천천히 귓가에서 멀어졌다.

돌아서는 홍란의 모습을 뒤로 한 채, 사공의 노가 강물을 힘차게 저었다.
```

## Final English reading copy

```markdown
# Chapter 460

It was bad weather in more ways than one.

The waters of Dongting Lake, which had swallowed dozens of vessels and claimed lives overnight, were rough, and the wind blowing in from the distance was violent.

Even the old boatman who knew Dongting Lake like the back of his hand seemed to think that setting out in such weather was a terrible idea.

“I—I can’t do it, sirs.”

Those were the first words from the boatman, who had clearly been dragged here against his will from the beginning. He continued anxiously,

“The places you wish to visit are unusually narrow and turbulent even for Dongting Lake… In weather like this, it would be even more impossible.”

“That is why we are asking for your help. Merchant ships and warships cannot enter those places, but a sturdy ferryboat guided by the most skilled boatman on Dongting Lake might be able to.”

“No matter how you put it…”

“Boatman?”

“Y-yes?”

“Please.”

A man remained a man, no matter how old he got.

The old boatman, dazed by Honglan’s gentle voice and dazzling beauty, only came to his senses after climbing aboard the ferryboat.

“What was I thinking? I must have gone mad. I knew what happened last night, yet I still set out on the water. What will I do if I run into a Hidden Shadow Ghost…?”[^1]

A Hidden Shadow Ghost?

The unfamiliar word mixed into his grumbling pricked my ears. When I turned around, my eyes met the terrified boatman’s.

He swallowed hard before answering.

“Just as the name says, it’s a ghostly creature. Plenty of boatmen have fallen victim to it lately. One of them was an old friend of mine. He went out at night hoping to earn a few extra coins, and then…”

The old boatman stared at the rippling waters of Dongting Lake with eyes steeped in fear.

“In any case, they call it a Hidden Shadow Ghost because people die without ever seeing even a shadow of it. This is only the humble opinion of an old man, but those recent incidents are clearly its doing. Every one of them was the work of that evil spirit.”

Gung Gibang clicked his tongue and cut in.

“Evil spirit, my ass. Listen, boatman. Do you think that’s the first story like this I’ve heard? If every one of those stories were true, half the fish in the world would have human faces, and the mountains would be crawling with thousand-year-old white tigers and dragons.”

“This is the absolute truth. With all these abominable things happening, the spirit of Dongting Lake must have grown furious.”

“An evil spirit wasn’t enough, so now we have a lake spirit too? Enough. Let’s not talk about it.”

“No, but every boatman in Hubei Province has heard this story…”

“Do I look like a boatman to you?”

“N-no, sir. Anyone can see that you’re a beggar among beggars.”

“Ah, that’s true, but now I’m suddenly pissed off.”

“P-please calm down, honored sir. This old man is guilty of nothing more than reporting what he heard.”

The old boatman’s voice was thick with grievance.

He had spent his entire life as a boatman in the Murim, where all sorts of legends and superstitions were treated as fact.

Perhaps because of that, he seemed to firmly believe that the recent string of gruesome incidents had been caused by the evil spirit known as the Hidden Shadow Ghost.

*When you think about it, it might not be complete nonsense.*

Judging by Honglan and Cheongpung’s expressions, they had reached the same conclusion.

The moment our gazes met, they both spoke at once.

“Benefactor, could it be…”

“Benefactor, is the Hidden Shadow Ghost the boatman mentioned…”

“Wait. I know what both of you are trying to say, so you don’t have to. And if you absolutely insist on calling me Benefactor, take turns. You’re confusing me.”

A single Benefactor parrot had already been enough. Now there were more of them.

Sometimes, things like this made me feel as though I had become someone important.

Then again, Honglan had good reason after I saved her life. But was that man Cheongpung really planning to treat me as his Benefactor for the rest of his life just because I had given him a few sweets when he was hungry?

I sighed and continued.

“Anyway, the Hidden Shadow Ghost is probably the Dongting Fisherman. Or it could be people taking advantage of the confusion to commit robbery.”

“That’s exactly what I was going to say, Benefactor.”

Not to be outdone by Cheongpung, Honglan nodded as well.

“I think so as well, Benefactor.”

“I said one person at a time.”

Regardless, the odds of this being a simple natural accident were slim.

From what we had heard so far, more than one boatman had died. The old boatman’s next words made the situation seem even more suspicious.

“Come to think of it, all the dead boatmen disappeared in roughly the same area. Hm? Wait a moment. The place you honored guests are heading toward is nearby too…”

The old boatman suddenly froze and slowly raised his head.

He looked us over one by one without a word, then quietly lowered the oar he had been holding to set off and stood up.

“Where are you going?”

At my question, the old boatman gave an awkward smile.

“Well, I seem to have forgotten to relieve myself.”

“Mujin.”

“Yes, Captain.”

“The boatman needs to pee.”

“Does he?”

By now, Hyuk Mujin and I understood each other perfectly.

When Mujin, who was practically a giant compared to the old boatman, blocked his way, the boatman’s eyes grew moist like those of a calf being led to the slaughterhouse.

“Do you still need to go?”

At Hyuk Mujin’s low voice, the boatman shook his head.

“…Come to think of it, I don’t.”

“Good. We’ll let you go before what you’re worried about happens, so don’t worry too much.”

I felt sorry for bullying an old boatman, but we needed an experienced guide to reach the Dongting Fisherman’s refuge.

Our destination was a narrow passage through which only a few ferryboats could pass.

Even if the government mobilized a hundred ships and tens of thousands of soldiers, they would not be able to enter. They would only become a burden.

*If we end up fighting the Dongting Fisherman, bringing more people will only increase the casualties.*

The government would seal off every route connecting Dongting Lake to the Yangtze in case he tried to flee. Then a small elite force, including Cheongpung and me, would pursue him and capture or kill him.

But just as important as dealing with the Dongting Fisherman was preventing any more pointless sacrifices.

Having finished thinking it through, I abruptly spoke.

“Hyuk Mujin, Gung Gibang, Young Lady Hong. You three…”

“No.”

“Where’s that dog barking?”

“I’ll contribute what little strength I have.”

The answers came before I could finish speaking, leaving me momentarily speechless. Hyuk Mujin and Gung Gibang clicked their tongues at my expression.

“It’s obvious. Completely obvious.”

“I can see exactly what you’re about to say.”

“We came all this way. How could we turn back now? What kind of man would that make me?”

“I feel the same. The Successor Beggar of the mighty Beggars’ Sect can’t be scared off by something like this.”

“Captain, you always tell us to stay out of anything that looks even a little dangerous. That’s your defining trait. Captain’s special.”

“You’re surprisingly timid.”

“But why have you been repeating everything I say since earlier, Young Hero Gung? It’s getting seriously annoying.”

“You damned bastard. Why pick a fight when things were going so well? Have you lost your mind?”

“Beggars’ Sect special. Not content with eating discarded food at inns, you pick up other people’s words too.”

“…I’ve never seen such a bastard who’s worse than a dog.”

“Regardless, I’m going with you no matter what you say, Captain. When I was young, a gifted fortune-teller read my fate and told me I would live in wealth and glory, eating well and living comfortably until I was over a hundred. There’s no way I’m dying today.”

Gung Gibang stared at Hyuk Mujin’s boast with an incredulous expression, then shook his head.

“Fine. I shouldn’t say anything. And I agree with that idiot, so don’t even think about leaving me behind. I’ve inherited the Beggars’ Sect’s finest arts. Even if I’m not as strong as you or Young Hero Cheongpung, I have no trouble protecting this one life of mine.”

“…”

I opened and closed my mouth without managing to say anything.

In truth, neither of them was weak enough to be dismissed.

Hyuk Mujin had begun learning martial arts relatively late, yet he had grown explosively while passing through countless crises alongside me. Gung Gibang was talented enough to become the Successor Beggar, as well as a Peak master who had entered a mature realm.

*But I’m afraid.*

I was afraid of losing people close to me. Afraid that what happened that day would repeat itself.

As I hesitated, Cheongpung suddenly spoke.

“Benefactor. If you go, I can follow you to the very depths of hell.”

“Young Hero Cheongpung.”

“Please don’t say no. I am a proper man and a martial artist too.”

“Young Hero Cheongpung.”

Cheongpung gave a small smile and shook his head.

“Benefactor, please don’t say anything. You trust us as much as I trust you. That’s all we need.”

“No, that isn’t what I meant. You’re obviously coming with us, so why did you step forward and…”

“Oh. Ah…”

“Don’t say anything pointless. Sit down and don’t ruin the mood.”

“…Yes, Benefactor.”

A quiet laugh escaped me at his crestfallen expression. I nodded toward Hyuk Mujin and Gung Gibang.

“Keep one thing in mind. In every situation, follow my judgment. Even if that means obeying an order to abandon me and run.”

“Captain, that…”

Gung Gibang discreetly jabbed Hyuk Mujin in the side.

“Of course we will. Hyuk will do the same, won’t he?”

“Hm? Ah, yes.”

It was obvious what was going on, but I pretended not to notice.

I would do everything in my power to prevent that situation from arising. I was confident I could separate them before they fell into danger.

But the last person was a problem.

“You already know what I’m going to say, don’t you?”

Honglan’s red lips slowly parted.

“You will need someone who knows the exact route.”

“It’s fine. According to you, Young Lady Hong, the finest boatman on Dongting Lake is already with us.”

“What if something unexpected happens?”

“I’ll deal with it.”

“Although I am insignificant compared to you and the others, I have also reached the First Rate realm…”

“I know. And I also know that this First Rate master spent several shichen submerged in the river while holding on to a strong man, and has only been conscious for half a shichen.”

“…”

Honglan bit down softly on her lip, struck where it hurt.

She knew better than anyone.

Being able to move around as she did now was entirely different from fighting a fierce battle.

“Once again, I suppose all I can do is watch.”

“Once again?”

“Yes. Back then, long ago. Last night. And now.”

Honglan read the question in my eyes and smiled. It was more bitter than any smile I had seen from her before.

“A great many things happened before a little girl who lost her clan and her parents overnight could become the woman she is today…”

“Ah.”

“Please excuse me for a moment.”

She looked up at me with shining eyes and quietly reached out a hand.

Her pale, slender fingers brushed through my tangled hair and along my neck. My body shuddered before I could stop it.

“Young Lady Hong, what are you…”

“All done. Ah, much better. Would you like to take a look?”

I followed Honglan’s fingers with my gaze and looked down at the clear waters of Dongting Lake.

Someone’s reflection floated on the surface.

My hair was neatly arranged, held in place by a single beautiful silver hairpin.

When I raised my head, Honglan was smiling brightly.

“Benefactor—no, Great Hero Jin.”

Her hair, which had come loose at some point, swayed softly in the wind. It billowed, shimmered, and gradually seemed to grow radiant.

“I wish you good fortune in battle.”

Her quiet voice slowly faded from my ears.

With Honglan’s departing figure behind me, the boatman’s oar struck the water with all his strength.

[^1]: “Hidden Shadow Ghost” is a literal rendering of a local name for a killer said to strike without being seen.
```
