<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0531.txt",
      "sha256": "ff721aa4ac5a2ae9dc11515735be8e28419342329137d623fb50dc42db562049",
      "bytes": 12836
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5f8232dd3d2e0b73590b88c3f78b122b1467eb2adf5968b534e806b6b4c1aa6c",
      "bytes": 3692
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "45b6bf942b171f3de42d49b20dbbb26d00990fab5102d28bea7ef78ef4cd3ae7",
      "bytes": 169746
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "1d5cf12bacd98b7293d70ca3bfff80e172023d10cf3c55248b68221edd186cb3",
      "bytes": 686
    },
    {
      "path": "characters/Hwangbo Ak.md",
      "sha256": "702d3423e05e32ad18e1db89c267e89f112bfd6f11e7aa7733f585e9e6e8dda9",
      "bytes": 761
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "32b5dc9056495cad6c71eb8fc8cb70ad9f1ce731951749e38f66d742482ad8c4",
      "bytes": 921
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e41a091b5ad363467e0ea19003cc627d7e5917821afccc7ccd359eefd017a7f1",
      "bytes": 159269
    }
  ],
  "estimated_tokens": 9881
}
-->

# Durable State Update — Chapter 531

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 531. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 531. Profile updates may replace only one
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
  "chapter": 531,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 531,
    "continuity_sources": [531],
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
    "The Mount Song Resolution formally restored the Murim Alliance; Mae Jonghak is its Alliance Leader, and Song Ho commands the Hidden Shadow Pavilion under his authority.",
    "Jin Taekyung and Cheongpung's prominent role in raising the Murim Alliance flag made them objects of intense attention among Murim factions.",
    "Taekyung believes the Zhongnan Sect resents him, the Jin Family of Taiyuan, and Jeok Cheongang after its repeated humiliations and will obstruct them.",
    "Cheongpung created Mimi Step from Mimi's movements; it is a snake-like footwork technique fast enough that Taekyung could barely track it with his naked eyes, and Cheongpung has recently lost his appetite while refining it.",
    "Mungyeong ended Taekyung's direct training and assigned him a final task of incorporating martial principles into his learned martial arts.",
    "Zhuge Feng's Demon-Sealing Formation still blocks all mana from the exposed Gate, while Jang Taebo is summoning artisans to process the Water God Dragon's remains.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Unnamed, Hong Dao's practical Disciple, is a scarred Supreme Peak master and Jung Ho's young Martial Uncle after enduring Repentance Cave and receiving Shaolin's Great Restoration Pill.",
    "The Black Dragon Demon Gate remains a major unorthodox power descended from the Demonic Cult's Twelve Branches; Wudang's second report identifies Jang Sam as the Killing Ghost and links his transformation to the Blood Fish.",
    "Jin Taekyung remains a Supreme Peak master with Three Flowers Gather at the Crown, advanced qi perception, exceptional resistance to monster Fear, and public S-rank-level recognition despite retaining an A-rank license.",
    "Ju Hwaran is eagerly awaiting Taekyung at an inn; Baek Woo and Hwangbo Ak are longtime friends and fellow Ten Dragons and Phoenixes members, and Hwangbo resents Taekyung while Baek fears provoking him.",
    "Hwangbo Ak was thrown from Gowolru and attacked by an unidentified gigantic man; Taekyung stepped between them and refused to move."
  ],
  "continuity_sources": [
    530,
    529
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Who is the gigantic man attacking Hwangbo Ak at Gowolru, and why is he targeting him?",
    "How will Taekyung incorporate Mungyeong's martial principles, and what effect will the custom pill have on him?"
  ],
  "safe_through": 530,
  "temporary_decisions": [
    "Render 숭산결의 as Mount Song Resolution, 고월루 as Gowolru, and 취팔선보 as Drunken Eight-Immortals Step; retain footwork technique for 보법.",
    "Render 탈진 as the capitalized system status Exhaustion; retain Ten Dragons and Phoenixes, Blazing Flame Divine Dragon, Dark Heaven, Murim Alliance, and Old Master.",
    "Render 홍적 as Hong Jeok, 모용영휘 as Murong Yeonghwi, and 복마전 as demon-slaying battleground.",
    "Render 새외무림 as Outer Murim, 새외 as Outer Lands, 북해빙궁 as North Sea Ice Palace, 야수묘왕 as Beast Miao King, and retain Nanman Beast Palace for 남만야수궁.",
    "Render 쌀벌레 as Rice Weevil and 만두 벌레 as dumpling grub; retain the chapter's blunt profanity and monster-comparison humor."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 주화란    | **Ju Hwaran**      |
| 종남파    | **Zhongnan Sect**                |
| 무림맹    | **Murim Alliance**               |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 삼류     | **Third Rate**    |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 장문인    | **Sect Leader**                              |
| 사형     | **Senior Brother**                           |
| 상태               | **Status**                     |
| 하남     | **Henan**              |
| 정마대전   | **Great Faction War**         |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 황보악 | **Hwangbo Ak** | Lesser Family Head of the Hwangbo Family and member of the Ten Dragons and Phoenixes. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 노호검객 | **Roaring Fury Swordsman** | Fiery-tempered elder and top-five master of the Zhongnan Sect. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 태을무정검 | **Taeeul Merciless Sword** | Title of the Zhongnan Sect’s Second Martial Uncle, who is in Xi’an. |
| 황보 | **Hwangbo** | Surname form used when addressing Hwangbo Eom. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 대초자곤 | **two-section staff** | Weapon carried by Sama Pyo's giant subordinate. |
| 내성 | **Inner City** | Fortified inner district of the Murim Alliance. |
| 황보세가 | **Hwangbo Family** | Hwangbo Ak's established martial family and the long-standing hegemon of Shandong. |
| 산동권룡 | **Shandong Fist Dragon** | Hwangbo Ak's sobriquet among the Ten Dragons and Phoenixes. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 주화란 | 궁기방 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Gung Gibang among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 황보악 | Young_Bureau_Head_to_Ten_Dragons_and_Phoenixes_member | Young Hero Hwangbo | formal-polite | Hwaran politely asks whether something is wrong. |
| 황보악 | 주화란 | admirer_to_Young_Bureau_Head | Young Lady Ju | formal-polite and deferential | Hwangbo addresses Hwaran while concealing his irritation. |
| 궁기방 | 황보악 | fellow_Ten_Dragons_and_Phoenixes_member | you | familiar-polite | Gung Gibang uses 자네 when asking Hwangbo what he is doing outside Gowolru. |

## Listed compact profiles

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 530
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung, uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and Dark Heaven’s Hubei forces, and has now found a trace of Honglan.

### Hwangbo Ak.md

# Hwangbo Ak (황보악)

- **Safe through:** Chapter 530
- **Aliases:** Shandong Fist Dragon
- **Role:** Hwangbo Ak is the Lesser Family Head of the Hwangbo Family, a member of the Ten Dragons and Phoenixes, and a young martial prodigy.
- **Personality:** Proud, self-obsessed, status-conscious, and easily humiliated.
- **Voice:** Polite and ceremonious in public but sharp, dismissive, and indignant when challenged.
- **Relationships:** Baek Woo is his longtime friend and fellow Ten Dragons and Phoenixes member; he is infatuated with Ju Hwaran, resents her apparent preference for Jin Taekyung, and carries a lasting grudge against Jin Mukyung after their Heaven's Gate Temple encounter.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 529
- **Aliases:** Hwaran
- **Role:** Level 88 Young Bureau Head and leader of the Yongbong Escort Bureau, responsible for its personnel and contracts after Heo Jun’s betrayal and now investigating at least two escort captains suspected of aiding his scheme.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather and rescued the Guangdong Chen Family’s surviving child, who became Song Ilseom’s grandmother; Ju Hogun is her father, Heo Jun was her uncle, and Jin Taekyung’s earlier reassurance remains emotionally vivid to her as she eagerly awaits seeing him again.

## Korean source

```text
＃531화



“너, 비켜.”

“나, 싫어.”

“……어?”

이런 반응은 예상하지 못했나 보다.

거한은 어린아이 주먹만 한 눈동자를 뒤룩뒤룩 굴리며 말을 더듬거렸다.

“시, 싫어?”

“응. 싫어. 안 비켜.”

“이, 이상하다. 지금까진 다 비켰는데.”

이건 또 무슨 캐릭터야.

‘얘도 지력을 안 찍었나?’

조상 중에 트롤이 있나 싶을 정도의 덩치에 비해, 보여 주는 언행은 유치원생이 따로 없다.

나는 우물쭈물하는 거한을 바라보며 턱을 긁적였다.

‘별 희한한 놈 다 보겠네.’

무림에서 별의별 인물들을 만났던 터라 이젠 제법 내성이 생겼다고 생각했는데, 이런 놈은 또 처음 본다.

하지만 지금은 개인적인 흥미보다 이 소란을 가라앉히는 것이 우선이었다.

“자, 천천히 물러나.”

“물러나?”

“그래.”

정의의 사도 흉내 낼 생각 따위는 없다. 딱히 사명감이 넘쳐 흐르는 것도 아니고.

하지만 이곳은 하남 대로변 한복판이다. 계속 싸움이 이어졌다가는 양민들 사이에서 인명 피해까지 일어날 수 있었다.

“무슨 사정이 있는지는 모르겠지만 이쯤 하자고. 괜찮지?”

나는 사근사근 말을 건네며 궁기방에게 눈짓했다.

눈치 빠르게 신호의 의미를 알아차린 궁기방이 미처 자리를 피하지 못하고 주저앉아 있는 양민들을 대피시킨다.

그 모습을 바라보던 거한이 커다란 눈동자를 이리저리 굴렸다.

“저놈이. 모욕했다.”

막대기처럼 굵은 손가락이 가리키는 방향에는 허리를 숙인 채 잔기침을 내뱉는 황보악이 있었다.

“모욕했다고?”

“근본 없는 사마외도, 우둔하기 짝이 없는 돼지. 네놈이 눈을 부릅뜨면 어쩔 거냐.”

“아하.”

“주군이 그랬다. 싸우기 전에 세 번 생각해 보라고. 그래서 세 번 생각하고 싸웠다. 칼도 저쪽에서 먼저 뽑았다.”

대충 상황이 어떻게 돌아갔는지 알 만하군.

짧은 단어의 나열이었지만 이해하기에는 그것만으로도 충분하다.

황보악은 산동 지방을 주름잡고 있는 황보세가의 소가주. 십봉룡에 들 만큼 무재도 뛰어난 무림판 금수저가 사마외도의 무림인에게 시비를 거는 건 쉽게 상상할 수 있는 일이다.

뭐, 궁기방도 황보악에 관해 좀 재수 없는 놈이라고 이야기한 적도 있고.

‘그나저나 이 녀석, 사파 쪽 인물이었군.’

어쩐지 뿜어내는 기세가 심상치 않더라니.

지금까지 흑도의 삼류 칼잡이들을 제외하면 제대로 된 사마외도(邪魔外道)의 무림인을 만난 적이 없던 터라, 불쑥 고개를 드는 호기심을 억지로 가라앉혀야 했다.

문득 뇌리를 스치는 한 가지 생각 때문이었다.

“혹시, 다른 사람도 건드렸나?”

“다른 사람?”

“그래. 저자와 같이 있던…… 다른 사람들이 있었을 텐데.”

가슴이 작게 뛴다. 미처 토해 내지 못한 주화란이라는 이름 세 글자가 혀끝에서 맴돌았다. 고개를 갸웃거린 거한이 눈을 깜빡였다.

“있었다. 남자 둘. 하나는 강했고 하나는 약했다. 그리고…….”

“그리고?”

“예쁜 여자. 엄청 예쁜 여자.”

“새끼, 보는 눈은 있어 가지고.”

“어?”

“아냐. 그래서, 그 사람들도 너와 싸웠나?”

“아니다. 저놈만 때렸다. 예쁜 여자. 얼굴만큼이나 착했다.”

안전하구나. 마음속으로 안도의 한숨을 내쉰 나는 거한의 어깨를 두드려 주었다.

“그래, 그래. 잘했다. 우리 어린이 참 착해요.”

“잘했다? 나, 착해?”

“어우, 그럼. 그러니까 이제 그만 화해하자. 알겠지?”

“으음. 으으음.”

얼추 거의 다 넘어왔군.

사마외도라길래 그냥 때려눕혀야 하나, 생각했는데 햇님 반 유치원생 대하듯이 살살 달래 주는 것으로도 충분했다.

거한이 고민이 가득 담긴 눈동자를 뒤룩뒤룩 굴리던 바로 그때였다.

“이게 무슨 짓거리요!”

등 뒤에서 울려 퍼지는, 누군가의 노기 가득한 외침.

고개를 돌리자 어느새 신형을 바로 세운 황보악이 활활 타오르는 눈동자로 이쪽을 바라보고 있었다.

“열화신룡! 지금 본 공자의 귀가 잘못된 거요? 사마외도의 편을 들다니!”

이쪽은 초면인데, 저쪽은 구면인 모양이다.

뭐, 어차피 피차 자기소개할 만큼 느긋한 상황은 아니니 오히려 잘됐다.

나는 황보악을 향해 덤덤하게 손짓해 보였다.

“일어나셨네. 그럼 얼른 와서 화해해요.”

“화, 화해?”

“얘기 들어 보니까 그럴 만한 사정이 있던데, 뭘. 괜히 소란 일으키지 말고 이쯤에서 마무리 지읍시다. 남자답게 악수 한 번 하고 끝내요. 좋게좋게.”

하지만 황보악은 야스오를 픽 했다가 패드립이라도 들은 사람처럼 눈을 부릅떴다.

“당신이 어찌 이럴 수 있소!”

“이럴 수 있어요. 좋게 말할 때 오세요.”

“같은 정파의 동도가 사마외도에 의해 해를 입었거늘. 어찌 저 간악한 사파 종자의 편을 든단 말이오!”

“사파면 어떻고, 정파면 어떻습니까. 다 같은 무림맹 한 식구인데. 그 노래도 못 들어 보셨어요? 우리는 모두 친구. 맞아 맞아.”

“그런 노래가 어디 있소! 그리고 한 식구라니! 사마외도 놈들이 정마대전 때 한 짓을 잊었소?”

“잊긴 뭘 잊어요. 겪어 본 적도 없는데. 혹시 그쪽은 정마대전 때 참전했습니까? 그럼 생각보다 동안이시네.”

“말도 안 되는 소리 집어치우고 비키시오! 본 공자는 저놈을 반드시 무릎 꿇려 사죄를 받아 내야겠으니!”

후욱.

갑자기 머리 위에서 따뜻한 바람이 분다. 나보다 머리 하나, 아니 두 개는 더 큰 거한이 뿜어낸 콧김이었다.

“무릎 꿇려? 네가. 나를?”

아주 잠깐, 움찔하던 황보악이 이를 악물었다.

“오냐. 아까는 네놈이 간악하게도 기습한 탓에 밀리긴 했지만, 본 공자를 건드린 것을 죽어서도 후회하게 만들어 주마!”

“안 되겠다. 너. 죽인다.”

거한의 눈동자가 차갑게 가라앉은 그 순간이었다.

쐐애애액, 쉭!

귓가를 파고드는 한 줄기의 파공성.

빛살처럼 쏘아진 황보악의 신형이 맹렬하게 뒤집혔다. 채찍처럼 휘둘려지는 다리에는 유형화된 공력이 서려 있었다.

‘각법(脚法)?’

황보세가는 대대로 권각의 고수를 배출해온 유서 깊은 무가.

황보악이 펼친 것은 그들을 산동성의 패자로 군림할 수 있게 한 황보세가의 비전 무공이 틀림없었다.

하지만…….

“너! 죽인다!”

상대가 좋지 않다.

내가 파악한 거한의 무위는 황보악에 비해 결코 떨어지지 않는다. 아니, 오히려 한 수에서 두 수를 앞선다고 해도 과언이 아니다.

그런 거한의 손에는 어느새 덩치와 어울리는 거대한 대초자곤(大梢子棍)이 들려 있었다.

후웅!

빠르고, 강맹하다.

공간을 뭉개듯이 나아가는 대초자곤에서 거한이 지닌 엄청난 힘과 속도가 느껴진다.

마침내 찾아온 격돌의 순간, 마지막까지 지켜보던 나는 조용히 두 팔을 뻗었다.

꽈앙!

굉음과 함께 막대한 기파(氣波)가 휘몰아쳤다. 땅바닥에 널브러져 있던 자재와 먼지, 흙 따위가 반경 삼 장 밖으로 밀려나고 사람들이 헛숨을 삼켰다.

그리고 그 사이로, 파르르 떨리고 있는 두 쌍의 눈동자가 있었다.

어떻게?

거한과 황보악의 눈에 담긴 의문. 경악으로 가득 찬 두 사람의 눈빛이 각각 단단한 손아귀에 붙잡힌 대초자곤과 다리를 향한다.

단 한 번의 움직임으로 모든 공격과 싸움을 막아낸 것이다.

“이, 이게.”

“강하다! 너, 강하다!”

흔들리는 그들의 눈빛을 마주하며, 나는 천천히 입을 뗐다.

“자, 이제 화해합시다.”

아. 한마디 덧붙이는 걸 깜빡했다.

“나한테 맞아 뒈지기 싫으면.”

“……!”

“……!”

친절한 말보다는, 친절한 말과 주먹으로 더 많은 것을 얻을 수 있는 법이다.

잠시 멍하니 나를 바라보던 거한이 더듬더듬 입을 열었다.

“화, 화해하겠다. 나, 착하다.”

“그래, 착하네. 그럼 나쁜 어린이가 되고 싶은 사람은?”

자연스럽게 향한 내 시선에 황보악의 입술이 앙다물어졌다.

“열화신룡, 당신 정말 이럴 생각…….”

“앗. 추가 정보가 도착했어요! 지금까지 만난 나쁜 어린이는 모두 내 손에 뒈지도록 맞고 착해졌답니다!”

“……생각해 보니 내 잘못도 있는 것 같소.”

“잘됐네, 그럼.”

그제야 나는 굳게 잡고 있던 대초자곤과 발목을 놓아주었다.

거한은 얼떨떨한 눈으로 계속해서 나만 힐끔거렸고, 황보악은 치욕에 몸을 떨고 있었지만 다시 싸움을 계속할 엄두를 내지는 못했다.

다만 분노와 두려움이 섞인 눈빛으로 나를 노려보며 입만 달싹일 뿐이었다.

“열화신룡 당신, 이러고도 정파라 할 수 있소?”

“놀랍네. 그건 내가 할 말인데.”

“그래, 그렇군. 아마 그대는 본 공자가 누구인지 몰라 이러는 듯한데…….”

“황보악. 나이는 스물아홉. 황보세가 소가주. 별호는 산동권룡.”

“……!”

“아, 최근에 몽정함.”

“아니야!”

“아니면 말고.”

불끈 움켜쥔 황보악의 주먹이 파르르 떨렸다.

“본 공자가 누구인지 알면서도 이런 모욕감을 줬단 말인가!”

“병신에는 성별도, 나이도, 정파와 사파도 없다. 이게 내 지론인데 아무래도 딱 맞는 것 같네.”

계속 놔뒀으면 영혼까지 탈탈 털렸을 놈이다. 괜히 일이 커지기 전에 막아 줬더니 별의별 헛소리를 다 듣네.

‘그런데 왜 희한하게 화가 안 나지.’

잠깐 고민하던 나는 그 이유를 깨달았다.

생각보다 너무 병신이라서. 그리고 그다지 신경 쓰이지도 않을 만큼 별것 아닌 놈이라서.

‘벌레.’

나에게 있어 황보악은 딱 그 정도다. 손가락으로 툭 쳐도 죽어 버리는 개미. 무심코 휘두른 손에 맞아서 빈사 상태에 이르는 모기.

거인들과 오랜 시간을 함께하다 보니 나 역시 거인이 되어 버렸다. 마치 소인국에 도착한 걸리버가 된 듯한 기분이랄까.

눈앞에 있는 황보악 역시 그 범주를 벗어나지 못한다.

그래서인지 황보세가의 소가주이자 십봉룡 중 한 사람이라는 신분도 그리 큰 감흥이 들지 않았다.

‘그냥, 남들보다는 조금 큰 소인 정도.’

그것이 걸리버가, 내가 황보악을 바라보는 시선이다. 그리고 어쩌면 조금은 그런 내 생각이 눈빛을 통해 느껴졌을지도 모르겠다.

황보악의 얼굴이 분노로 거무죽죽하게 물들었다.

“다, 당신…….”

“충고 하나만 할까?”

“뭐?”

“누울 자리 보고 다리 뻗어.”

“이, 이자가!”

큰 소리가 터져 나왔지만 나는 눈 하나 깜짝하지 않고 말을 이었다.

지금부터 하는 말은 황보악이 뼈에 새겨 놓아야 한다.

“노호검객. 태을무정검. 많이 들어 본 이름이지? 아, 요즘은 자주 못 들어 봤을 수도 있겠다. 한창 요양 중이니까.”

“……!”

“옆에 산동권룡 추가하고 싶지 않으면 헛수작 부리지 마. 처음이자 마지막 경고다.”

솨아아아.

오직 한 사람을 향해 집중한 기세에, 황보악이 헛숨을 삼킨다.

녀석 역시 종남파 장문인의 두 사형이 어찌 되었는지 들어 봤음이 틀림없다.

거기에 더해 다시 한번 깨달았을 것이다.

천하 무림은 합당한 대의명분. 그리고 힘의 법칙으로 돌아간다는 것을.

툭.

나는 몸을 부르르 떠는 황보악의 어깨를 두드리며 웃었다.

“힘들어 보이네. 다른 사람한테는 내가 말해 둘 테니까 돌아가라.”

“하, 하지만.”

“가.”

황보악이 할 수 있는 것은 이를 악문 채 떠나는 것뿐이었다.

그리고 유난히 작아 보이는 녀석의 등이 멀어졌을 때, 한 사람의 목소리가 귓가에 닿았다.

“진 대협!”

오랜만에 듣는, 그래서 더 반가운 목소리였다.
```

## Final English reading copy

```markdown
# Chapter 531

“You. Move.”

“No. I don’t want to.”

“……Huh?”

He clearly hadn’t expected that response.

The giant’s eyes, each as large as a child’s fist, rolled around as he stammered.

“Y-You don’t want to?”

“Yeah. I don’t want to. I’m not moving.”

“That’s s-strange. Everyone moved until now.”

What kind of character was this?

*Did he forget to put any points into intelligence, too?*

For someone with a build so massive that I wondered whether he had a troll among his ancestors, his behavior was nothing short of childish.

I scratched my chin as I watched the giant fidget.

*I’m seeing all kinds of weirdos today.*

I thought I’d developed a decent tolerance after meeting all sorts of people in the Murim, but this guy was a first.

Still, settling down this commotion took priority over my personal curiosity.

“Come on. Back away slowly.”

“Back away?”

“Yeah.”

I had no intention of pretending to be some agent of justice. It wasn’t as though I was overflowing with a sense of duty.

But this was the middle of a main street in Henan. If the fight continued, civilians could end up getting hurt.

“I don’t know what happened, but let’s stop here. All right?”

I spoke gently and glanced at Gung Gibang.

Quick to catch on, Gung Gibang understood what I meant and began evacuating the civilians who had been unable to escape and were still sitting on the ground.

The giant watched him, his huge eyes rolling from side to side.

“That guy. Insulted me.”

The thick finger pointed toward Hwangbo Ak, who was bent over and coughing weakly.

“He insulted you?”

“Rootless practitioner of demonic, heterodox arts. Pig as stupid as they come. What are you going to do if you glare at me?”

“Ah.”

“My lord said to think three times before fighting. So I thought three times and fought. He drew his sword first, too.”

I could more or less figure out what had happened.

The words were short and disjointed, but they were enough to understand the situation.

Hwangbo Ak was the Lesser Family Head of the Hwangbo Family, which held sway over the Shandong region. It wasn’t hard to imagine a Murim golden spoon with enough martial talent to join the Ten Dragons and Phoenixes picking a fight with a martial artist from the demonic, heterodox side.

Besides, Gung Gibang had once called Hwangbo Ak a real pain in the ass.

*So this guy is from the unorthodox faction.*

No wonder the aura he gave off had been so unusual.

Aside from some Third Rate dark-path figures, I had never met a proper martial artist who practiced demonic, heterodox arts. I had to forcibly suppress the curiosity that suddenly rose inside me.

One thought had crossed my mind.

“Did you lay a hand on anyone else?”

“Someone else?”

“Yeah. There must have been…… other people with him.”

My heart gave a small beat. The three syllables of Ju Hwaran’s name, which I had been unable to voice, lingered at the tip of my tongue.

The giant tilted his head and blinked.

“There were. Two men. One was strong, and one was weak. And……”

“And?”

“A pretty woman. A very pretty woman.”

“Damn. At least you have good taste.”

“Huh?”

“Nothing. So, did you fight them, too?”

“No. I only hit that guy. The pretty woman. She was as kind as she was beautiful.”

She was safe.

I let out a sigh of relief inwardly and patted the giant on the shoulder.

“Yeah, yeah. Good job. What a good little boy.”

“Good job? I’m good?”

“Of course you are. So let’s stop fighting and make up now. Got it?”

“Hmm. Hmmmm.”

I had almost won him over.

Since he was from the unorthodox faction, I had wondered whether I should simply knock him down. But gently coaxing him like a kindergartner from the Sunshine Class was enough.

It was at that exact moment, as the giant rolled his eyes full of serious thought, that a furious shout rang out from behind me.

“What do you think you’re doing?”

I turned around. Hwangbo Ak had already straightened up and was glaring in our direction, his eyes blazing.

“Blazing Flame Divine Dragon! Are my ears deceiving me? You’re taking the side of a demonic, heterodox practitioner!”

He was a stranger to me, but apparently I wasn’t to him.

Well, neither of us was in a situation relaxed enough for introductions, so that was convenient.

I calmly gestured toward Hwangbo Ak.

“You’re up. Come over here and make up with him.”

“M-Make up?”

“From what I’ve heard, he had his reasons. Don’t cause any more trouble. Let’s wrap things up here. Be a man, shake hands once, and call it done. Let’s keep things friendly.”

But Hwangbo Ak opened his eyes wide like someone who had locked in Yasuo and then gotten hit with a family insult.

“How can you do this?”

“I can do it just fine. Come over while I’m asking nicely.”

“A fellow orthodox martial artist has been harmed by a practitioner of demonic, heterodox arts. How can you take the side of that vile unorthodox whelp?”

“What does it matter whether he’s from the unorthodox faction or the orthodox faction? We’re all one family in the Murim Alliance. Haven’t you heard that song? We are all friends. That’s right, that’s right.”

“What song are you talking about? And members of the same family? Have you forgotten what those demonic, heterodox bastards did during the Great Faction War?”

“Forgot? I’ve never even experienced it. Did you take part in the Great Faction War? You look younger than I expected.”

“Stop talking nonsense and move! This Young Master must make that bastard kneel and apologize!”

Whoosh.

A warm breeze suddenly blew over my head. It was the giant’s breath.

He was one head taller than me. No, two.

“Kneel? You. Me?”

Hwangbo Ak flinched for the briefest moment, then gritted his teeth.

“Fine. You may have pushed me back earlier because you launched a despicable surprise attack, but I’ll make you regret provoking this Young Master even in death!”

“No. You. I kill.”

The giant’s eyes turned cold.

Fwoosh—whoosh!

A piercing sound tore into my ears.

Hwangbo Ak’s body, shooting forward like a ray of light, twisted violently. His leg lashed out like a whip, wrapped in visible internal energy.

*A kicking technique?*

The Hwangbo Family was a venerable martial family that had produced masters of punches and kicks for generations.

What Hwangbo Ak had unleashed was undoubtedly the Hwangbo Family’s secret martial art—the very technique that had allowed them to reign as the hegemon of Shandong Province.

But……

“You! I kill!”

He had picked the wrong opponent.

From what I could tell, the giant’s martial prowess was in no way inferior to Hwangbo Ak’s. If anything, it would not be an exaggeration to say he was a move or two ahead.

And in the giant’s hands was now a massive two-section staff to match his enormous frame.

Whoosh!

Fast and powerful.

The two-section staff advanced as though crushing the space around it, revealing the giant’s tremendous strength and speed.

At the moment of impact, after watching until the very last instant, I quietly extended both arms.

Boom!

A deafening roar erupted, followed by a massive wave of qi. Materials, dust, and dirt scattered across the ground were blasted beyond a three-zhang radius, and the people nearby sucked in startled breaths.

And in the middle of it all were two pairs of trembling eyes.

How?

The question in the giant’s and Hwangbo Ak’s eyes was unmistakable. Both of them stared in shock at the staff and leg caught in solid grips.

With a single movement, I had stopped every attack and brought the fight to an end.

“This…….”

“Strong! You, strong!”

Meeting their wavering gazes, I slowly opened my mouth.

“Now, let’s make up.”

Ah. I’d forgotten to add one thing.

“If you don’t want me to beat you to death.”

“……!”

“……!”

You could get more done with kind words and a fist than with kind words alone.

The giant stared blankly at me for a moment before stammering,

“I-I will make up. I’m good.”

“Yeah, you’re good. Now, who wants to be a bad little boy?”

My gaze naturally turned toward Hwangbo Ak. His lips pressed into a tight line.

“Blazing Flame Divine Dragon, are you really planning to—”

“Oh! An additional piece of information has arrived! Every bad little boy I’ve met so far has been beaten half to death by me and turned good!”

“……Come to think of it, I suppose I bear some responsibility as well.”

“Good. Then we’re settled.”

Only then did I release the two-section staff and ankle I had been gripping tightly.

The giant kept stealing bewildered glances at me, while Hwangbo Ak trembled with humiliation. But he didn’t dare resume the fight.

He only glared at me with a mixture of anger and fear, his lips moving soundlessly.

“Blazing Flame Divine Dragon, after this, can you still call yourself orthodox?”

“Wow. That’s exactly what I was about to ask you.”

“Very well. I suppose you’re acting this way because you don’t know who this Young Master is……”

“Hwangbo Ak. Twenty-nine years old. Lesser Family Head of the Hwangbo Family. Sobriquet: Shandong Fist Dragon.”

“……!”

“Oh, and he recently had a wet dream.”

“That’s not true!”

“If you say so.”

Hwangbo Ak’s clenched fist trembled.

“You knew who I was, and you still chose to humiliate me like this?”

“A fucking idiot has no gender, age, or allegiance to the orthodox or unorthodox factions. That’s my creed, and it seems to fit you perfectly.”

If I’d let the fight continue, he would’ve had his soul beaten out of him. I had stopped things from getting worse, only to hear all kinds of ridiculous nonsense.

*But why am I not angry?*

After thinking about it for a moment, I realized why.

Because he was even more of an idiot than I’d expected. And because he was so insignificant that he wasn’t worth getting worked up over.

*An insect.*

That was all Hwangbo Ak was to me. An ant that would die if I flicked it with my finger. A mosquito that would be brought to the brink of death by a careless swing of my hand.

After spending so much time alongside giants, I had become a giant myself. It felt as though I had become Gulliver after arriving in Lilliput.

The Hwangbo Ak standing before me was no different.

Perhaps that was why his status as the Lesser Family Head of the Hwangbo Family and a member of the Ten Dragons and Phoenixes failed to impress me.

*Just a Lilliputian who’s a little bigger than the others.*

That was how Gulliver—and I—looked at Hwangbo Ak.

And perhaps some of what I was thinking had been visible in my eyes.

Hwangbo Ak’s face darkened with rage.

“You…….”

“Want some advice?”

“What?”

“Know who you’re dealing with before you pick a fight.”

“You bastard!”

A roar erupted, but I didn’t even blink as I continued.

Hwangbo Ak needed to carve what I was about to say into his bones.

“The Roaring Fury Swordsman. The Taeeul Merciless Sword. You’ve heard those names a lot, haven’t you? Well, maybe not lately. They’re both busy recovering.”

“……!”

“If you don’t want to add the Shandong Fist Dragon to their number, don’t try anything funny. This is your first and last warning.”

Whoosh.

Hwangbo Ak sucked in a startled breath as the aura I focused solely on him pressed down.

He must have heard what had happened to the Sect Leader of the Zhongnan Sect’s two Senior Brothers.

And now, he had realized once again that the Murim of the world operated according to two things:

A just and legitimate cause.

And the law of strength.

Tap.

I patted Hwangbo Ak’s trembling shoulder and smiled.

“You look like you’re having a hard time. I’ll explain things to the others, so go home.”

“B-But—”

“Go.”

There was nothing Hwangbo Ak could do but grit his teeth and leave.

And when his back, looking unusually small, had disappeared into the distance, a familiar voice reached my ears.

“Sir Jin!”

It was a voice I hadn’t heard in a long time—which made it all the more welcome.
```
