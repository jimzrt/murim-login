<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0465.txt",
      "sha256": "74ca8085d41534614dce6d26caf77af97937be1110ba446c8a720d24d3202760",
      "bytes": 13375
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "8806c60a2c45e5c98f9a380e2b49949f258116c36ac586e760ebed2e93119e5b",
      "bytes": 4225
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "6c0cb257a02660ef755aa478d8acc524022f1f817067b94ad1a7af9551ef6dee",
      "bytes": 150993
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "b8ef826f2cf42fd911fdd2158a6b341ed6915c08e7c49766ff3a9754ec5a7658",
      "bytes": 553
    },
    {
      "path": "characters/Dongting Fisherman.md",
      "sha256": "791c9d8914901efc48978045a4e0f466b13325eae9272166e47bb63f2b940f8a",
      "bytes": 703
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "923e9d1f3656684e7c794faaac8a93a7a41defa2795e3725f6fe7df610e1b0b7",
      "bytes": 146076
    }
  ],
  "estimated_tokens": 9953
}
-->

# Durable State Update — Chapter 465

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 465. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 465. Profile updates may replace only one
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
  "chapter": 465,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 465,
    "continuity_sources": [465],
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
    "Taekyung has entered the Dongting Fisherman’s underwater secret refuge and confirmed that the Dongting Fisherman is inside; a white streak of light has just struck Taekyung’s attacking spearhead, so the confrontation’s outcome is unresolved.",
    "Fresh damage throughout the refuge’s passage bears the traces of one person’s deliberate force, but its cause and connection to the Dongting Fisherman remain unknown.",
    "Taekyung completed the unavoidable Peak-grade Quest The Tragedy of Dongting Lake, rescued the only two survivors found, and earned the Water Rescue Worker Title.",
    "Honglan survived the Dongting Lake disaster and is recovering; Ju Wongong remains unconscious under guard after passing the most dangerous stage of his injuries.",
    "Jin Wikyung is acting as an inspector for the new Murim Alliance and is cooperating with Taekyung’s investigation.",
    "The shared symbols between the Arch Lich’s magic circle and Dark Heaven’s formations remain unexplained.",
    "The Sea Serpent Society and three Yangtze River Channel League strongholds, including Donghu Stronghold, were destroyed with more than a thousand casualties, while the perpetrators’ wider plans remain unknown.",
    "Mungyeong is searching Donghu Stronghold for Dark Heaven traces with Zhuge Clan and Wudang; Mungyeong found no land evidence or Moving Formation remnants and entered the river to search the remaining area.",
    "Wudang is responding to an unidentified killer demon responsible for more than thirty deaths, including twenty pilgrims on Mount Wudang.",
    "The Skeleton King’s undead identity remains concealed, and Taekyung has ordered him to join Peace Guild under a prepared contract.",
    "Go Jun is expected to succeed Lee Jungryong as Ares Guild’s captain and is searching China for Lee’s holographic recorder.",
    "The captured Three Fiends is a former-generation great fiend and Supreme Peak Dark Heaven subordinate whom Taekyung is transporting alive to investigate possible codes or markings."
  ],
  "continuity_sources": [
    464,
    463
  ],
  "open_questions": [
    "What is the Dongting Fisherman’s exact role in Dark Heaven, and who launched the white streak that interrupted Taekyung’s attack?",
    "What caused the single person’s deliberate destruction inside the refuge, and is it connected to the Dongting Fisherman or another intruder?",
    "What are the origin and purpose of the symbols shared by the Arch Lich’s magic circle and Dark Heaven’s formations?",
    "Who destroyed Donghu Stronghold and the related Yangtze River Channel League strongholds, why was no Moving Formation trace left, and was the destruction a diversion?",
    "What danger did Mungyeong detect, and are the Wudang killer demon and that danger connected to Taekyung, Jeok Cheongang, or Dark Heaven?"
  ],
  "safe_through": 464,
  "temporary_decisions": [
    "Render 오기조원 as Five Qi Returning to Origin, 노화순청 as Furnace Fire Pure Blue, 반로환동 as Returned to Youth, and 복자 as diviner.",
    "Render 살귀 as killer demon, 은영귀 as Hidden Shadow Ghost, 일급 낭인 as First Rate wandering martial artist, 삼괴 as Three Fiends, 대마두 as great fiend, and 마군 as Demon Lord.",
    "Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”",
    "Preserve the Skeleton King’s grandiose, mock-offended voice and Taekyung’s dry, profane humor; render 주원공 as Ju Wongong, 대죽산표국 as Daejuksan Escort Bureau, 형문검가 as Hyungmun Sword Family, 응성상회 as Eungseong Merchant Association, 천룡인 as Celestial Dragon, 사인교 as four-person sedan chair, 홍란 as Honglan, 가기 as singing courtesan, 구족 as the nine branches of kin, 수상 구조대원 as Water Rescue Worker, and 수공 as water arts.",
    "Render 익양루 as Yiyang Tower, 황철 as Hwang Cheol, 도립군 as Do Ripgun, 광수도귀 as Mad Water Saber Demon, 파랑호 as Wave Fox, 동정호 as Dongting Lake, 사천혈사 as Sichuan Blood Tragedy, 천령폭 as Tianling Falls, and 기경팔맥 as Eight Extraordinary Meridians."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 열화문    | **Fire Gate Clan**               |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 초식     | **form**                                         | Numbered technique movement                           |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 보상               | **Reward**                     |
| 사천     | **Sichuan**            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동정어옹 | **Dongting Fisherman** | Publicly condemned the Yangtze River Channel League and disappeared three days before this chapter. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 사천당문 | **Sichuan Tang Clan** | Martial clan cited for its poison-based cleansing method. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 염화일로 | **Flamefire Path** | Fire Gate Clan signature movement technique; Jeok Cheongang has reached its ninth stage. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 단혼사 | **Soul-Severing Thread** | Tang Jinhu's silver-thread hidden weapon. |
| 화룡갑 | **Fire Dragon Armor** | Jin Taekyung's renamed bound armor, formerly the Black Dragon Armor. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 동정채 | **Donghu Stronghold** | Stronghold where Mu Song's Uncle Hwang is based. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 흑목조간 | **black-wood fishing rod** | The Dongting Fisherman's distinctive weapon; the broken rod is his only known trace. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 464
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Dongting Fisherman.md

# Dongting Fisherman (동정어옹)

- **Safe through:** Chapter 464
- **Aliases:** None
- **Role:** The Dongting Fisherman is a previous-generation Supreme Peak master whose water arts rival the Seafaring King; he is identified as Dark Heaven's tail and suspected perpetrator of the Dongting Lake attack, with hidden refuges throughout the lake.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** The Dongting Fisherman opposed the Yangtze River Channel League and was monitored by the Lower District Sect for several years after friction with it, while current records place him in Hubei Province.

## Korean source

```text
＃465화



쾅!

강렬한 충격과 함께 창날의 방향이 꺾인다.

실로 기괴한 투로(鬪路)를 그리며 날아든 빛줄기가, 살아 있는 생물처럼 꿈틀거리며 머리 위로 쏟아졌다.

쉬쉬쉬슁!

강기의 소나기. 일순간 어두운 동굴을 환하게 밝히는 그 파괴적인 힘 앞에서, 나는 부드럽게 몸을 비틀었다.

쉭, 퍼버버버벅!

어깨, 목, 허리와 가슴…….

전신의 요혈을 아슬아슬하게 스쳐 지나간 빛줄기가 단단한 동굴 바닥을 꿰뚫고 부수었다.

조금이라도 반응이 늦었다면 즉사했을 공격.

하지만 동정어옹의 공격은 내 털끝 하나도 건드리지 못했고, 순간의 위기는 기회로 이어졌다.

바로 지금처럼.

후웅-!

아까의 충격으로 흔들린 백염의 창날이 허공에서 뚝 꺾여 나가며 동정어옹의 목을 노렸다.

어느새 신형을 돌린 그의 회백색 눈동자가 부릅떠짐과 동시에, 새하얀 빛줄기가 황급히 창날을 가로막았다.

하지만…….

‘그 정도로는 부족하지.’

동정어옹이 기나긴 세월 동안 막대한 공력을 쌓은 노괴(老怪)라면, 나는 시스템 보상과 사선을 넘나드는 싸움 끝에 그 세월을 뛰어넘은 괴물이다.

공력이 비등하다 해도 내 육신에는 인간의 한계를 뛰어넘은 거인의 힘이 깃들어 있다.

꽈앙-!

청백색의 화염과 빛줄기가 닿은 순간, 하늘이 쪼개지는 듯한 굉음이 들리며 동정어옹의 신형이 튕겨져 나갔다.

자그마한 노인의 체구가 단단한 암석을 부수고 벽면에 처박혔다. 그와 동시에 동굴이 흔들리고 커다란 종유석들이 쏟아졌다.

나는 그 너머로 비치는 회백색 눈동자를 노려보며 또박또박 내뱉었다.

“일어나. 되지도 않는 연기는 집어치우고.”

투두두둑.

조금 전만 하더라도 죽은 듯이 축 늘어져 있던 사지가 힘차게 움직였다.

충격으로 인해 움푹 팬 벽면에서 몸을 일으킨 동정어옹은 목을 좌우로 꺾었다.

우드득, 뼈 어긋나는 소리와 함께 걸음을 옮기는 그의 주름진 손에는 어느새 기다란 낚시대 한 자루가 쥐어져 있었다.

‘흑목조간(黑木釣竿).’

만년한철에 비할 바는 아니지만, 그 강도가 운철(隕鐵)에 버금가며 극히 유연하다는 동정어옹의 독문병기다.

일부가 파손되었음에도 길이는 일 장에 달했고, 끝에는 은은한 빛을 띤 낚싯줄과 바늘이 걸려 있었다.

‘저건……….’

본 적은 없어도, 들어 본 적은 있다. 사천당문이 자랑하는 단혼사와 어깨를 나란히 한다는 천잠사(天蠶絲)라는 귀물을.

한낱 누에고치가 천잠이라는 거창한 이름으로도 부족해 영물 취급받는 것도 신기했지만, 그 실이 강철로도 끊지 못할 정도로 질기고 예리하다는 것만큼 놀랍진 않았다.

흑목조간에 연결된 낚싯줄이 바로 그 천잠사였다.

‘주의해야겠군.’

조심해서 손해 볼 것은 없다. 화룡갑이 신병이기라고 해도 무엇이든지 막아 낼 수 있는 무적의 갑옷은 아니니까.

나는 삼 장 앞에서 멈춰선 동정어옹을 응시하며 입을 열었다.

“두 가지 선택지가 있다. 첫 번째는 이 자리에서 내 손에 뒈지는 것. 두 번째는 알고 있는 모든 사실을 하나도 빠짐없이 털어놓고 희생자들에게 속죄하는 것. 둘 중 뭐로 할래?”

“…….”

대답 대신 흐릿한 회백색 눈동자가 나를 물끄러미 바라보았다.

어떤 감정도 느껴지지 않는, 도무지 인간의 것이라고 믿기 힘든 그 눈빛에 순간 서늘한 기운이 등골을 타고 솟구쳤다.

‘……뭐지, 이 느낌은?’

사람이라면 누구나 감정이 있기 마련이다.

하지만 동정어옹은 달랐다. 분명 숨을 쉬고, 생기(生氣)가 느껴짐에도 그는 속이 텅 비어 있는 물건 같았다.

‘도대체 이게 무슨…….’

오래 고민할 틈이 없었다. 다음 순간, 나는 흠칫하며 창대를 꽉 움켜쥐었다.

몇 발자국 떨어지지 않은 곳에서 갑작스럽게 움직인 이름 모를 물고기 한 마리 때문이었다.

뼈가 드러나고, 배 어림의 살점이 뜯겨나간 상태로 몇 번인가 펄떡이던 물고기는 그대로 움직임을 멈췄다.

누군가가 물어뜯은 선명한 이빨 자국을 몸에 남긴 채.

‘설마?’

동정어옹을 바라본 나는 미간을 좁혔다. 주름진 입가에 묻은 붉은 핏물과 반짝이는 비늘.

그제야 오는 길에 들었던 소리의 정체와 조금 전까지 그가 무엇을 하고 있었는지 깨달을 수 있었다.

‘생으로 뜯어먹고 있던 거군. 그것도 살아 있는 물고기를.’

뭐 이런 미친 늙은이가 다 있지?

문득 틈만 나면 케이블 영화 채널에서 틀어주던 고전 판타지 영화가 머릿속을 스쳤다.

지금 와서 다시 보니 그 영화에 나온 괴물이랑 좀 닮은 것 같기도 하다. 왜소한 체구 하며, 구부정한 허리와 듬성듬성한 머리카락까지.

작게 혀를 찬 내가 동정어옹을 향해 입을 열었다.

“이러면 장르가 바뀌는데…… 혹시 너희가 이번에 찾고 있는 신물이 반지는 아니지?”

“…….”

“그래, 대답하지 마라. 어차피 잠시 후에 얼마 남지 않은 네 머리카락을 한 가닥씩 뽑으면서 물어볼 계획이거든.”

“크윽.”

“오, 미친. 뭐야.”

나는 갑작스러운 동정어옹의 반응에 눈을 크게 떴다.

아무 말이나 나오는 대로 뱉고 본 건데, 탈모인의 역린을 제대로 건드린 건가?

하지만 동정어옹이 정말 모근의 위협에 반응한 것인지, 또 다른 이유 때문이었는지는 알 수 없었다.

내가 뭐라 말을 잇기도 전에, 늙은 회백색 눈동자가 부릅떠지며 엄청난 고함이 터져 나왔으니까.

“크아아아아-!”

쿠구구구궁!

이건 새벽마다 동네 뒷산에서 소리 지르시는 으악새 할아버지의 외침이 아니다.

고강한 공력이 실린 외침이 공기를 타고 동공을 후려쳤다. 바닥, 벽면, 가릴 것 없이 주위의 모든 것이 흔들리고 터져 나갔다.

그리고 그 여파가 시작되기도 전에, 동정어옹의 신형은 희끗한 잔상을 남기며 나를 향해 쏘아지고 있었다.

쏴아아아악!

어느덧 시커멓게 물든 눈동자.

빛줄기와 함께 쇄도하는 동정어옹을 향해, 나는 깊게 가라앉은 목소리로 입을 열었다.

“볼륨 줄여. 이 씨부럴 새끼야.”

화륵, 콰아아아!

청백색의 화염이 투명한 창날 위로 덧씌워짐과 동시에, 나는 걸음을 뗐다.

팟!

삼 장은 결코 짧다고 할 수 없는 거리다.

그러나 나도, 동정어옹도 초절정이라는 영역에 발을 디딘 초인(超人). 우리가 서로를 향해 쏘아진 순간, 모든 것은 무의미했다. 간격이 지워지고 바람이 터져 나갔다.

초고온의 열기가 실린 백염의 창날과 살아 있는 생물처럼 꿈틀거리는 천잠사가 수 갑자의 공력을 머금고 공간을 갈랐다.

쉬쉬쉬쉬슁!

극쾌(極快)라 부를 만한 속도. 흑목조간의 끝에서 시작된 천잠사가 파도처럼 출렁인다.

지금까지 상대했던 숱한 병기에서 느낄 수 없었던 기괴막측한 움직임. 동정채를 뒤덮은 숱한 시신들에 남아 있던 상흔(傷痕)이 문득 눈앞을 스친다.

‘바로 이 무공으로…… 약하고 죄 없는 양민들을 죽인 거군.’

나는 감수성이 풍부한 사람도, 성인군자도 아니다. 장강수로채의 수적들을 옹호할 만한 이유도 없다. 그들은 약탈을 위해 모인 수적 집단이고 분명 누군가의 목숨과 재물을 빼앗았을 테니까.

누군가의 목숨을 빼앗은 것 같으나, 나와 차이가 있다면 그들의 살인은 살아남기 위해서가 아니라 필요에 의해 자행되었다는 점이다.

하지만…….

‘사람이, 그렇게 죽어서는 안 되는 거였다.’

개미처럼 짓밟히고, 가축을 도살하듯 베여 죽은 이들이 수백. 동정호의 한복판에서 수장된 이들이 또한 수백이다.

그리고 그들 대부분은 무림인이 아니었다. 무공이라고는 일초반식도 모르는 양민들이었고 제 이름조차 쓸 줄 모르는 어린아이 역시 있었다.

그런 사람들이, 그런 식으로 죽어서는 안 되는 거다.

사람이, 사람을 그리 죽일 수는 없는 거다.

“알겠냐. 개새끼야.”

느려진 세상 속, 목소리가 휘몰아치는 바람에 파묻혔다.

창대를 틀어쥔 손아귀에 강한 힘이 실린다. 전신에서 강대한 열양지기가 끓어오르는 것을 느끼며, 나는 창날을 비스듬히 내리그었다.

화륵, 서걱!

허공에 피어오른 한 줄기 불꽃. 동시에 흩어지는 빛줄기.

창날이 그린 궤적을 따라 잘려 나간 천잠사의 일부가 나풀나풀 흩날린다.

너무도 쉽게 초식을 파훼 당한 동정어옹이 괴성을 내지르며 재차 흑목조간을 휘둘렀다.

슁, 쉬쉬쉬쉬슁!

빛줄기가 사방을 갈랐다. 강기를 머금은 천잠사가 공간을 가르며 막아서는 모든 것을 꿰뚫고 베었다.

그러나 나는 그 모든 공격을 피하며, 묵묵히 창을 휘둘렀다.

서걱! 서걱! 서걱!

선명하게 보인다. 낚싯대의 형태를 한 저 기병(奇兵)이 어디로 향할지, 그와 이어진 천잠사가 어떤 움직임으로 나를 노릴지.

반개한 두 눈동자는 모든 상황을 빠짐없이 받아들이고, 활짝 열린 감각은 이어질 공격을 읽어 냈다.

‘중단전(中丹田)이 닫혀 있었을 때의 나였다면, 분명 힘들었겠지.’

서 있는 자리가 바뀌면 보이는 풍경도 달라지는 법.

중단전의 개방은 감각의 확장과 나조차 알지 못했던 새로운 시야를 선물해 주었고, 그 결과가 눈앞에 나타나고 있었다.

‘온다.’

흑목조간과 같은 특이한 병장기는 처음에는 익히기 어렵지만, 무기의 이점을 극대화시킴과 동시에 알맞은 무공을 익힌다면 상대하기가 매우 까다롭다.

하지만 나는 짓쳐 드는 궤적을 정확히 예측하고 창을 휘둘렀다.

서걱!

“크아아아악!”

빠르고 예리한 일격에 다시 한번 잘려 나가는 천잠사.

이렇다 할 피해도 주지 못하고 오 장에 달하던 천잠사가 절반 가까이 줄어들자, 동정어옹의 전신에서 한층 더 광포해진 기세가 흘러나왔다.

“그래, 이래야 좀 사람 같네.”

하지만 무공은 심신(心身)이 안정되었을 때 더욱 큰 위력을 발휘하는 것이다.

마음이 흔들리면 몸도 흐트러지고, 그만큼 움직임이 크고 거칠어진다.

그리고 내게 있어 헐거워진 그물의 틈을 찾는 것은 그리 어려운 일이 아니었다.

쐐애애애액!

염화일로(炎火一路).

축축한 동굴 바닥 위를 한 줄기의 불꽃이 가로지른다.

공력 소모가 극심하고 투로 역시 단순하지만, 열화문의 무공 대부분이 그러하듯 염화일로에도 가장 큰 장점 두 가지가 있었다.

‘쾌속하고, 파괴적이다.’

콰아아아!

뜨거워진 공기와 함께 주위의 모든 수분이 증발한다.

사막의 모래처럼 푸석해진 지면을 밟으며 나는 화살처럼 쏘아졌다.

쉭!

고개를 틀자 목덜미를 노리던 천잠사가 스쳐 지나갔다.

공격에 실패한 동정어옹은 황급히 천잠사의 방향을 틀어 내 전신을 휘감으려 했지만, 나는 그보다 반 박자 빠르게 발을 굴렀다.

퍼엉! 서걱!

얼음장처럼 차가운 무언가가 발끝을 통해 전해지더니, 이내 불처럼 뜨거워진다.

맨발이던 엄지발가락 끝부분의 살점이 깔끔하게 잘려 나간 것이다.

평범한 사람이었다면 비명을 내질렀을 만큼 상당한 통증이 밀려왔지만 나는 덤덤하게 받아들였다.

‘이 정도는 아무것도 아니야.’

그간 현대와 무림을 오가며 숱한 부상과 고통을 감내해 온 나다.

모든 신경 다발이 잘려 나가는 듯한 고통에 몸부림치고, 진심으로 죽고 싶다고 생각한 적도 있었다.

그랬던 내게 이 정도 상처쯤은 아무것도 아니다. 아니, 오히려 턱없이 값싼 통행료라고 할 수 있었다.

고작 엄지발가락 일부를 잃은 것으로, 이 생사결의 향방을 결정지을 수 있는 기회를 얻었으니까.

‘지금!’

머리에서 내린 명령을 따라 손과 발이 물 흐르듯 나아간다.

어느 때보다 쾌속하고 군더더기 없는 움직임. 나는 뒤로 젖힌 창대를 있는 힘껏 흩뿌렸다.

쐐애애애액, 뻑!

그야말로 섬전 같은 일격. 내 손을 떠난 백염이, 위기를 느끼고 거리를 벌리려던 동정어옹의 어깨를 부수며 벽면 깊숙이 틀어박힌다.

“끄아아아악!”

고통에 찬 비명을 들으며, 나는 놈을 향해 주먹을 치켜세웠다.

“볼륨 줄이랬지.”

“……!”

뻐억!
```

## Final English reading copy

```markdown
# Chapter 465

*Boom!*

The direction of White Flame’s spearhead was knocked aside by the force of the impact.

A streak of light that had flown in along a truly bizarre trajectory writhed like a living creature before raining down over my head.

*Shh-shh-shh-shing!*

A downpour of Force.

Faced with that destructive power, which illuminated the dark cave in an instant, I smoothly twisted my body.

*Swish. Boom-boom-boom!*

My shoulder, neck, waist, and chest…

The streak of light swept within a hair’s breadth of the vital acupoints throughout my body before piercing and smashing through the solid cave floor.

An attack that would have killed me instantly if I had reacted even a moment later.

But the Dongting Fisherman’s attack failed to touch even a single hair on my body, and that moment of danger turned into an opportunity.

Just like now.

*Whoom!*

White Flame’s spearhead, shaken by the impact a moment earlier, snapped sharply through the air and went for the Dongting Fisherman’s throat.

His grayish-white eyes widened as he turned his body, and a snow-white streak of light hurriedly flew across to block the spearhead.

But…

*That won’t be enough.*

If the Dongting Fisherman was an old monster who had accumulated massive amounts of internal energy over a long lifetime, then I was a monster who had surpassed those years through System rewards and countless battles fought on the edge of death.

Even if our internal energy was equal, my body housed the strength of a giant that had surpassed the limits of humanity.

*Boom!*

The instant the blue-white flames touched the streak of light, a thunderous boom rang out like the sky itself had split apart, and the Dongting Fisherman’s body was sent flying.

The small old man’s body smashed through the solid rock before crashing into the wall. At the same time, the cave shook, and huge stalactites came tumbling down.

I glared at the grayish-white eyes visible beyond the falling debris and spoke slowly and clearly.

“Get up. Quit the pathetic act.”

*Crack-crack-crack.*

Only a moment earlier, his limbs had hung limp as though he were dead. Now they moved with vigor.

The Dongting Fisherman rose from the hollow his impact had left in the wall and cracked his neck from side to side.

With the sound of bones grinding against one another, he began walking. A long fishing rod had somehow appeared in his wrinkled hand.

*The black-wood fishing rod.*

It could not compare to Ten-Thousand-Year Cold Iron, but it was the Dongting Fisherman’s signature weapon, said to have a strength comparable to meteorite iron while being extraordinarily flexible.

Despite being partially damaged, it was still one zhang long. A fishing line and hook with a faint sheen hung from its tip.

*That’s…*

I had never seen it before, but I had heard of it.

The Heavenly Silkworm Thread, a rare treasure said to stand shoulder to shoulder with the Sichuan Tang Clan’s Soul-Severing Thread.

It was strange enough that a mere silkworm cocoon was treated as a spiritual treasure, as though even the grand name Heavenly Silkworm were insufficient. But that was not as surprising as the fact that its thread was so tough and sharp that even steel could not cut it.

The fishing line attached to the black-wood fishing rod was that very Heavenly Silkworm Thread.

*I’ll have to be careful.*

There was nothing to lose by being cautious. Even if Fire Dragon Armor was a divine weapon, it was not an invincible suit of armor capable of blocking everything.

I opened my mouth while staring at the Dongting Fisherman, who had stopped three zhang away.

“You have two choices. The first is to die by my hand right here. The second is to confess every single thing you know without leaving anything out, then atone to the victims. Which one do you want?”

“……”

Instead of answering, his hazy grayish-white eyes stared blankly at me.

There was no emotion in that gaze. For a moment, a chill rose along my spine at the sight of eyes that were impossible to believe belonged to a human being.

*…What is this feeling?*

Everyone had emotions.

But the Dongting Fisherman was different. He was clearly breathing, and I could sense life within him, yet he seemed like an object with nothing inside.

*What the hell is this…?*

I did not have time to think about it for long. The next moment, I flinched and tightened my grip on the spear shaft.

A nameless fish had suddenly moved only a few steps away.

The fish, its bones exposed and the flesh around its belly torn away, thrashed several times before stopping completely.

Clear teeth marks from where someone had bitten into it remained on its body.

*No way.*

I looked at the Dongting Fisherman and narrowed my eyes.

Red blood and glinting scales clung to the wrinkles around his mouth.

Only then did I realize what the sound I had heard on the way here was—and what he had been doing until just moments ago.

*He was tearing it apart and eating it raw. A live fish, at that.*

What kind of crazy old man was this?

Suddenly, a classic fantasy movie that had been played constantly on the cable movie channels flashed through my mind.

Now that I thought about it, he did look a little like the monster from that movie. His small frame, his hunched back, even his sparse hair.

I clicked my tongue softly and spoke to the Dongting Fisherman.

“This changes the genre… The divine treasure you people are looking for isn’t a ring, is it?”

“……”

“Fine, don’t answer. I was planning to ask you while plucking out the few hairs you have left, one by one.”

“Guh.”

“Oh, shit. What was that?”

I opened my eyes wide at the Dongting Fisherman’s sudden reaction.

I had just blurted out whatever came to mind. Had I somehow hit a balding man’s sore spot?

But I had no way of knowing whether the Dongting Fisherman had reacted to the threat to his hair roots or for some other reason.

Before I could say anything else, his old grayish-white eyes widened, and an enormous roar burst from his throat.

“GRAAAAAH!”

*Rumble-rumble-rumble!*

This was not the cry of the old man who shouted from the hill behind the neighborhood every morning at dawn.

The roar, infused with powerful internal energy, traveled through the air and slammed into the cavern. Everything around us shook and burst apart—the floor, the walls, everything.

And before the shock wave could even begin to spread, the Dongting Fisherman’s body shot toward me, leaving behind a pale afterimage.

*Whoooooosh!*

His eyes had turned pitch-black.

As the Dongting Fisherman charged toward me with the streak of light, I spoke in a low, sunken voice.

“Turn down the volume, you sibu-leol bastard.”

*Fwoosh! Boom!*

The blue-white flames coated the transparent spearhead, and I stepped forward.

*Pop!*

Three zhang was not a short distance.

But the Dongting Fisherman and I were both superhuman beings who had set foot in the realm of Supreme Peak. The moment we shot toward each other, distance became meaningless. The gap vanished, and the air exploded.

White Flame’s spearhead, charged with extreme heat, and the Heavenly Silkworm Thread, writhing like a living creature while holding several *jiazi* of internal energy, tore through space.

*Shh-shh-shh-shh-shing!*

The speed was worthy of being called extreme swiftness.

The Heavenly Silkworm Thread, extending from the tip of the black-wood fishing rod, surged like a wave.

Its bizarre, unfathomable movements were unlike anything I had ever felt from the countless weapons I had faced before.

The scars left on the countless corpses scattered throughout Donghu Stronghold flashed before my eyes.

*He killed weak and innocent commoners with this martial art.*

I was neither a particularly sensitive person nor a *junzi*. I had no reason to defend the bandits of the Yangtze River Channel League. They were a group of river bandits who had gathered to plunder, and they had undoubtedly taken someone’s life and property.

It might seem as though I had taken lives too, but the difference between me and them was that they had not killed to survive. They had done it because it served their purposes.

But…

*People should not have died like that.*

Hundreds had been trampled like ants and cut down like livestock. Hundreds more had been drowned in the middle of Dongting Lake.

And most of them had not been martial artists. They were commoners who did not know even a single form of martial arts. There had even been children who could not write their own names.

People like that should not have died in such a manner.

A person could not kill another person like that.

“You get it, you son of a bitch?”

In the slowed world, my voice was buried beneath the raging wind.

Power surged through the hand gripping the spear shaft. Feeling the mighty Scorching Yang Qi boiling throughout my body, I brought the spearhead down at an angle.

*Fwoosh. Shhk!*

A single spark blossomed in the air.

At the same time, the streak of light scattered.

A section of the Heavenly Silkworm Thread was severed along the path traced by my spearhead and fluttered away.

The Dongting Fisherman, whose form had been countered so easily, let out a strange scream and swung the black-wood fishing rod again.

*Shing. Shh-shh-shh-shh-shing!*

Streaks of light split the air in every direction.

The Heavenly Silkworm Thread, filled with Force, sliced through space, piercing and cutting through everything that stood in its way.

But I avoided every attack and silently swung my spear.

*Shhk! Shhk! Shhk!*

I could see it clearly.

I could see where that strange weapon shaped like a fishing rod would go, and what movements the Heavenly Silkworm Thread attached to it would make as it came for me.

My half-open eyes took in every detail of the situation, while my senses, opened wide, read the attacks that were about to follow.

*If this were me before my Middle Dantian opened, it would have been difficult.*

When the place where you stand changes, the scenery you see changes as well.

Opening my Middle Dantian had expanded my senses and given me a new field of vision I had not even known existed. The result was unfolding right before my eyes.

*Here it comes.*

A strange weapon such as the black-wood fishing rod was difficult to master at first. But if one maximized its advantages and learned the appropriate martial arts, it became extremely difficult to deal with.

But I accurately predicted the trajectory rushing toward me and swung my spear.

*Shhk!*

“GRAAAAAAAH!”

The Heavenly Silkworm Thread was cut again by a fast, razor-sharp strike.

Without inflicting any meaningful damage on me, the thread that had once stretched five zhang had been reduced by nearly half. An even more ferocious aura poured from the Dongting Fisherman’s entire body.

“Now that’s more like a person.”

But martial arts displayed greater power when the mind and body were stable.

When the mind shook, the body lost its balance as well, and one’s movements became larger and rougher.

Finding a gap in the loosened net was not difficult for me.

*Whoooooosh!*

*Flamefire Path.*

A single streak of flame raced across the damp cave floor.

Its internal energy consumption was tremendous, and its trajectory was simple, but like most of the Fire Gate Clan’s martial arts, the Flamefire Path had two major advantages.

*It’s fast and destructive.*

*Boom!*

The air grew hot, and all the moisture around us evaporated.

I stepped onto the ground, now dry and crumbly as desert sand, and shot forward like an arrow.

*Swish!*

I turned my head, and the Heavenly Silkworm Thread that had been aimed at the back of my neck brushed past.

The Dongting Fisherman failed to land his attack and hurriedly redirected the thread, trying to wrap it around my entire body.

But I kicked off the ground half a beat faster.

*Boom! Shhk!*

Something as cold as ice traveled through the tip of my foot, then quickly grew hot as fire.

The flesh at the tip of my bare big toe had been cleanly sliced away.

The pain was severe enough that an ordinary person would have screamed, but I accepted it calmly.

*This is nothing.*

I had endured countless injuries and unimaginable pain while traveling between the modern world and Murim.

There had been times when I writhed in agony as though every bundle of nerves in my body were being severed, times when I had genuinely wished to die.

Compared to that, an injury like this was nothing.

No—it was an absurdly cheap toll.

For the loss of only part of my big toe, I had gained an opportunity to decide the outcome of this life-and-death duel.

*Now!*

My hands and feet moved like flowing water, obeying the command sent from my brain.

My movements were faster and cleaner than ever, without a hint of wasted motion.

I pulled the spear shaft back, then whipped it forward with all my strength.

*Whoooooosh—thud!*

The strike was truly as swift as lightning.

White Flame left my hand, smashed through the Dongting Fisherman’s shoulder as he sensed the danger and tried to retreat, then buried itself deep in the wall.

“GRAAAAAAAH!”

Listening to his scream of pain, I raised my fist toward him.

“I told you to turn down the volume.”

“……!”

*Thud!*
```
