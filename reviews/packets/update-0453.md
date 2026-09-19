<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0453.txt",
      "sha256": "67bb1cf7f70ad4264f93086a9d3b00f7a2d1fe9fbb390be7110bc532b3bb8d24",
      "bytes": 14396
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a7a5802e52903df47e57a3798b03b41f3793703ea0f2ada513c4b3311edd53a6",
      "bytes": 2880
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "816dc4793d56aacf789240b63419c8e6d339182f0d89bf961108f129b32a1db4",
      "bytes": 148563
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "c8d721ade2e8543cb1456c35da77bdc06162d8e152889927c0e7dfa042aeb77c",
      "bytes": 944
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "cd4e20bd0b38ca2a128dd05baa835e0bbe8ba06959859cf95094e5ce19f663c4",
      "bytes": 609
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "4d0afadf6f2b4ea6fd639b8f247a13f7e16a6a071f64ea6d68811e2190d2cca1",
      "bytes": 1108
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e461e36fdfca1b36145d5e3c2c1ab27e0d867d36d7f0c4d6478c5994b61b21fa",
      "bytes": 142508
    }
  ],
  "estimated_tokens": 10653
}
-->

# Durable State Update — Chapter 453

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 453. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 453. Profile updates may replace only one
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
  "chapter": 453,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 453,
    "continuity_sources": [453],
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
    "Taekyung accepted Quest Another Chaos to uncover the truth behind the Hubei incidents and find the culprit.",
    "Jin Wikyung is acting as an inspector for the new Murim Alliance and is cooperating with Taekyung's investigation.",
    "The shared symbols between the Arch Lich's magic circle and Dark Heaven's formations remain unexplained.",
    "The Sea Serpent Society and the Yangtze River Channel League's Hubei strongholds were destroyed, while the Dongting Fisherman disappeared.",
    "Wudang is responding to an unidentified killer demon responsible for more than thirty deaths, including twenty pilgrims on Mount Wudang.",
    "The Skeleton King's undead identity remains concealed, and Taekyung has ordered him to join Peace Guild under a prepared contract.",
    "Go Jun is expected to succeed Lee Jungryong as Ares Guild's captain and is searching China for Lee's holographic recorder.",
    "Taekyung's party has escaped Tianling Falls, reached Zaoyang, and is traveling by land toward the Zhuge Clan.",
    "Qingxia Hall is an influential Hubei social club formed by the children of powerful families, whose members currently obstruct the party's departure through their public spectacle."
  ],
  "continuity_sources": [
    452,
    451
  ],
  "open_questions": [
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Who destroyed Donghu Stronghold and the related Yangtze River Channel League strongholds, and why was no Moving Formation trace left behind?",
    "Is the Dongting Fisherman a member of Dark Heaven, and who are the other Supreme Peak attackers?",
    "Is the killer demon attacking Wudang connected to Dark Heaven?",
    "What evidence is contained in Lee Jungryong's holographic recorder, and what are the terms of the Peace Guild–Wizard Guild agreement?"
  ],
  "safe_through": 452,
  "temporary_decisions": [
    "Render 황철 as Hwang Cheol, 도립군 as Do Ripgun, 광수도귀 as Mad Water Saber Demon, 파랑호 as Wave Fox, 동정호 as Dongting Lake, and 사천혈사 as Sichuan Blood Tragedy.",
    "Render 살귀 as killer demon and 일급 낭인 as First Rate wandering martial artist.",
    "Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”",
    "Preserve the Skeleton King's grandiose, mock-offended voice and Taekyung's dry, profane humor.",
    "Keep Peace Guild, guild house, Inventory, Magic Johnson, established martial-arts terminology, black magic, poison human, World Hunter Association, Wizard Guild, Sea Serpent Society, Red Cliffs, and Dongting Fisherman unchanged; render 현공진인 as “Perfected Being Hyeongong,” 화왕질리언 as “Fire King Zilean,” 청협방 as “Qingxia Hall,” and 조양 as “Zaoyang.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 화산파    | **Huashan**                      |
| 제갈세가   | **Zhuge Clan**                   |
| 삼류     | **Third Rate**    |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 신법     | **movement technique**                           |                                                       |
| 낭인     | **wandering martial artist**                     |                                                       |
| 표국     | **Escort Bureau**                            |
| 소국주    | **Young Bureau Head**                        |
| 은인     | **Benefactor**                               |
| 아이템              | **Item**                       |
| 화산     | **Huashan**            |
| 귀가      | **your family**                                                 |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 사서삼경 | **Four Books and Three Classics** | Confucian texts used to describe conventional scholarly learning. |
| 은자 | **silver nyang** | Silver currency unit. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천룡 | **Heavenly Dragon** | The ideal form Jeok Cheongang wishes Taekyung to become. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백주 | **baijiu** | Strong distilled liquor ordered at the inn. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 청협방 | **Qingxia Hall** | Unofficial Hubei social club formed by influential families' children. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 452
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 452
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Rival finalist alongside Baek Woo and Zhuge Gyun; trades insults with Taekyung and is helping investigate Tang Taesang’s murder through Beggars’ Sect intelligence.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 452
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

## Korean source

```text
＃453화



“야! 이 개애새끼들아아!”

순간 차가운 바람이 불었던 것 같다. 아니면 내 고함이 그렇게 느껴질 만큼 우렁찼거나.

아마 후자일 가능성이 크겠지.

솨아아아아.

은자를 줍기 위해 버둥거리던 수십 명의 사람이 움직임을 멈추고, 소란스러운 대로변에 침묵이 내려앉는다.

그리고 다음 순간, 내 입술 사이로 흘러나온 한마디가 짧은 정적을 깨트렸다.

“셋 센다.”

“……?”

“집합.”

“……!”

서당 개 삼 년이면 풍월을 읊고, 맞으면서 지내면 사서삼경도 외운다.

그것이 지난 일 년 동안 내 폭력과 욕설에 길든 서당 개, 아니 혁무진이 누구보다 빠르게 움직일 수 있는 이유였다.

“집하아압!”

비명 같은 복명복창과 함께 달려온 혁무진의 신형이 내 앞에서 딱 멈췄다.

이어 한 박자 늦게 사태를 파악하고 경신법을 발휘한 궁기방이 혁무진과 거의 동시에 도착했고, 청풍은…….

“전병! 전병 빨리 주세요! 은인 화났어요!”

시벌 놈이. 그 와중에 전병 챙기는 것 봐라.

나는 군것질거리를 포장한 뒤 빛살처럼 달려오는 청풍을 향해 부드럽게 말했다.

“천천히 와. 나 화 안 났으니까.”

“와아! 정말요?”

“응. 화난 게 아니라 존나 빡친 거야.”

“앗, 아앗…….”

나는 안절부절못하는 청풍과 슬그머니 시선을 회피하는 두 녀석을 바라보며 생각했다.

‘도대체 이 자식들은 언제쯤 사람이 될까.’

젖 먹던 힘까지 끌어 올려서 제갈세가로 달려가진 못할망정, 은자 몇 개 줍겠답시고 무공까지 쓰는 꼬락서니 봐라.

심지어 궁기방 저놈은 은근슬쩍 다른 사람 손에 있던 은자까지 뺏었다. 이 정도면 거지가 아니라 도적놈이다.

‘인생, 씨바…….’

최근 사원 복지를 위해 애썼건만, 결국 이렇게 되는구나.

맑은 하늘을 우러러본 나는 손바닥에 침을 뱉었다.

“혁무진. 이마 대.”

“예?”

고개를 번쩍 든 혁무진이 황당한 표정으로 되물었다.

“저만요?”

“응. 우선 너만.”

“궁 소협은요?”

“쟨 뼛속까지 거지잖아. 솔직히 거지가 은자 줍는다는데 뭐라 하기도 그래.”

“정확하고도 현명한 판단이로군.”

눈치를 보고 있던 궁기방이 엄숙한 목소리로 끼어들자 혁무진이 고리눈을 떴다.

“아니, 그렇긴 뭐가 그럽니까. 내가 거지라고 하면 맨날 화내면서.”

“내가? 무슨 말도 안 되는 소릴. 나는 머리부터 발끝까지 거지다. 태어날 때부터 거지였고 죽을 때까지 거지로 살 거야.”

“……거지 같네, 진짜.”

“칭찬 고맙군.”

“궁기방 거지새끼.”

“허어, 이리도 감미로울 수가.”

궁기방을 죽일 듯이 노려보던 혁무진이 재차 입을 열었다.

“그럼 청 소협은요?”

“청풍은 청풍이잖아.”

화산파고 자시고, 청풍은 원래 저런 놈이다.

모든 것이 함축된 한마디에 혁무진이 중얼거렸다.

“어이가 없는데 납득이 되네…….”

“보는 눈 많다. 빨리 끝내자.”

“몇 대요?”

“말해 봐. 네가 몇 대를 맞으면 반성할 수 있을지.”

“그럼 한 대?”

“세 대.”

“빌어먹을, 알겠습니다.”

“욕했으니까 다섯 대.”

“……그냥 열 대 때리십쇼. 맞고 뒈지게.”

“무인다운 결연한 태도에 가산점 부여한다. 그러니까 한 대. 몇 대?”

“한 대!”

힘차게 복명복창 한 혁무진이 이마를 내민 바로 그 순간이었다.

“거기, 멈추도록.”

“……?”

나는 손바닥을 내리며 돌아섰다.

쥐죽은 듯이 조용한 대로변의 한복판. 사인교에 올라탄 열 명의 남녀가 불쾌와 흥미로움이 뒤섞인 시선으로 이쪽을 바라보고 있었다.

그리고 자신들의 막대한 부를 과시하듯, 하나같이 호화로운 차림새를 한 그들 중에서도 유난히 눈에 띄는 한 청년이 있었다.

조금 전 내가 들었던 목소리의 주인이다.

“멈췄다. 왜?”

내 물음에 청년이 눈을 동그랗게 떴다. 자신이 들은 말을 믿을 수 없는지, 한동안 눈을 깜빡이던 그가 이내 피식 웃었다.

“본 공자가 누구인지 모르는 모양이군.”

“내가 그것까지 알아야 하나?”

“이런 오만방자한 놈을 보았나!”

청년이 한 말이 아니다. 나는 사인교를 박차고 솟구치는 신형을 바라보았다.

‘이건 또 뭐야.’

쉬쉭, 차창!

공중에서 세 차례나 제비를 돌며 착지한 뱁새눈의 사내가 타오르는 눈빛으로 검을 뽑았다.

그 화려한 동작에 지켜보던 사람들 사이에서 탄성이 터져 나온다.

“보아하니 떠돌이 무림인 같은데, 백주대낮에 소란을 일으키는 것으로도 모자라 감히 존귀하신 분께 망발을 내뱉…….”

“보석 많이 박았네. 그거 시선 교란용이냐?”

나는 검을 장식한 보석을 응시했다. 종류도 다양한 수십여 개의 보석들이 햇빛을 받아 빛을 뿜어내는 중이었다.

“뭐?”

“눈부시니까 집어넣으라고.”

따앙-!

뱁새눈의 사내가 눈을 부릅떴다.

내가 쏘아 보낸 탄지(彈指)의 힘을 이기지 못하고 손아귀를 빠져나간 검이 허공을 날아 지면 깊숙이 꽂혔다.

“썅노무 새끼가 어디서 함부로 검을 들이대. 그것도 이런 백주 대낮에.”

‘어쭈, 지랄한다.’

일류 언저리쯤 되려나?

나름대로 실력을 갈고닦은 것 같긴 한데, 극한의 겉멋충이 따로 없다.

“이, 이놈이……!”

“그리고 시끄럽게 군 건 너희지, 난 조용하게 만든 거고. 피차 일 복잡하게 만들지 말고 가라. 응?”

진심이었다.

지금까지 날파리 한두 마리 꼬여 본 줄 아나. 내 집도 아니고 지나가는 길이라면 굳이 달려드는 모기에 에프킬라까지 뿌릴 이유가 없다.

손으로 휘휘 젓고 가던 길이나 마저 가는 게 낫지.

하지만 아무리 진심을 전하려고 해도, 꼭 한 번에 알아듣지 못하는 놈들이 있기 마련이다.

차차차창!

수십 개의 검신이 사방에서 빛났다. 청색 비단 무복을 걸친 청협방의 무인들이 우리를 겹겹이 에워싸자, 당황했던 뱁새눈의 얼굴 위로 득의양양한 기색이 떠올랐다.

“제법 알려진 낭인 놈 같은데, 지금이라도 무릎을 꿇고 용서를 빌어라. 혹시 아느냐, 공자께서 너그러이 자비를 베푸실지.”

나는 뱁새눈의 어깨너머를 힐끗 바라보았다. 우두머리 격으로 보이는 청년을 필두로, 다른 남녀들이 반짝이는 시선으로 이곳을 바라보고 있었다.

저건 아무리 봐도 동물원 원숭이를 구경하는 관람객의 모습이다.

“글쎄, 저쪽은 딱히 그럴 생각이 없어 보이는데?”

“뭐?”

“물론 나도 그럴 생각은 없고. 그리고 지금까지 경험해 본 바로는 이게 가장 특효약이더라고. 안 그러냐?”

슬쩍 주먹을 들어 올리자 내 눈치만 살피고 있던 버뮤다 삼각지대가 격하게 호응했다.

“그렇지. 복날 개처럼 맞아야 정신을 차리지.”

“그 특효약 제일 처음으로 먹은 게 저였습니다. 바로 완치됐죠.”

“은인, 저 그럼 잠깐 만두 사러 다녀와도 돼요?

“아니. 그냥 있어. 어차피 금방 끝날 테니까.”

저벅.

“자, 잠깐!”

한 걸음을 내딛자 뱁새눈의 눈동자에 다급함이 서렸다.

삼류 건달패라면 상대의 수준을 모르니 오기로라도 달려들겠지만, 저 녀석은 일정 수준의 무공을 익힌 무인이다.

그렇기에 꽃병풍 역할을 하는 청협방 무인들도, 자신도 내 상대가 되지 못할 거라는 사실을 깨달은 것이 분명했다.

“우, 우린 청협방(靑俠房)이다!”

“어. 그래서?”

“아, 아니 청협방의 위명을 듣지 못했단 말이냐!”

“응. 내가 요새 귀가 잘 안 들려서.”

저벅.

“멈춰! 멈추라니까!”

“크흠.”

이렇게 되자 다급해진 것은 뱁새눈뿐만이 아니었다.

혀를 차며 상황을 지켜보던 제갈세가의 가솔이 헛기침과 함께 입을 열었다.

“제가 사정을 설명할 테니, 그만하시는 것이 좋을 듯 합…….”

뻑! 털썩!

“예? 혹시 방금 뭐라고 하셨어요?”

“…….”

주먹을 쥐고 우뚝 서 있는 나와, 코뼈가 주저앉은 채 혼절한 뱁새눈을 번갈아 바라보던 제갈세가의 가솔이 떨떠름하게 중얼거렸다.

“멈추시는 게 좋을 것 같다고…….”

“예?”

“아무래도 이것저것 문제의 여지가…….”

“예?”

“괜한 충돌은 삼가시는 편이…….”

“뭐요?”

“……아닙니다.”

“아, 예.”

피 묻은 주먹을 바짓단에 문질러 닦은 나는 주위를 돌아보았다.

궁기방은 저놈 저렇게 될 줄 알았다며 중얼거리고 있었고, 덕분에 목숨을 연장한 혁무진의 표정은 밝았다.

그리고 청풍은…….

“마! 어디 가!”

“헉, 은인!”

아니, 저 새끼 설마 지금 만두 사러 가는 거……?

기척도 내지 않고 슬금슬금 멀어지고 있는 청풍의 뒷모습을 보니 저게 정말 사람인지 의문이 들 정도다.

‘저 자식은 반드시 잡는다.’

결연한 의지와 함께 걸음을 떼자, 주위를 둘러싸고 있던 꽃병풍 무인들이 헛숨을 삼키며 길을 비켰다.

하지만 이 자리에 있는 청협방의 무인은 비단 그들뿐만이 아니었다.

“으하하! 재미있군, 재미있어. 너희도 그리 생각하지 않느냐?”

웃음을 터트린 청년의 물음에, 사인교(四人轎)를 짊어지고 있던 네 사람의 거한이 한 목소리로 대답했다.

“예, 주군.”

“이런 웃음을 준 귀인을 이리 보낼 수는 없지. 본 공자는 괜찮으니, 어서 가서 모셔오거라.”

“충(忠)!”

공력이 충만한 외침. 동시에 사인교를 내려놓은 거한들이 바람과도 같은 속도로 나를 향해 쇄도했다.

일개 가마꾼에서 뛰어난 절정 고수로 변모한 그들이 사방(四方)을 점하며 달려들었다.

후우우우웅!

강맹한 기운이 실린 각각의 일권(一拳)이 정교하게 맞물리며 휘둘려진 그 순간.

퍼버버벅!

정확히 네 번의 타격음과 함께, 네 개의 몸뚱어리가 달려든 속도 그대로 엎어졌다.

그리고 다시는 일어나지 못했다.

“뭐여, 시부럴.”

“……!”

“……!”

“……!”

완전한 정적이 찾아온 대로변.

의식을 잃은 거한들을 툭툭 걷어찬 내가 청년을 향해 어깨를 으쓱해 보였다. 한껏 올라갔던 그의 입꼬리는 어느새 파르르 떨리고 있었다.

“재밌네. 재미있어. 너희도 그렇게 생각하지?”

제갈세가의 가솔을 이마를 짚었고, 궁기방과 혁무진은 기계처럼 고개를 끄덕였다.

“내 삼십 년 거지 인생을 통틀어 가장 재미있다.”

“조장님. 저는 지금 배꼽 빠졌습니다. 어디로 굴러갔는지 통 안 보여서 계속 찾고 있어요.”

“그래, 요즘 같은 퍽퍽한 시기에 이런 큰 재미를 주신 분을 어떻게 그냥 보내겠냐. 그러니까…… 저 새끼 멱살 잡고 모셔와.”

“충성, 충성!”

“난 이제 모르겠다. 뭐 어떻게 되건 네가 알아서 다 하겠지.”

단 한 대도 맞기 싫은 혁무진은 누구보다 열의를 불태웠고, 궁기방은 투덜거리면서도 앞으로 나섰다.

처음 분위기와는 달리 완전히 뒤바뀐 상황.

믿고 있던 호위들까지 당하자 청협방의 남녀들은 고래고래 소리를 지르기 시작했다.

“노, 노옴! 내가 누군지 알고!”

“이 천하의 무뢰배야! 감히 대국의 법도를 거스르려 하느냐!”

“제, 제게 손을 댄다면 우리 가문이 가만히 있을 것 같은가요!”

한 놈만 잡으려고 했는데, 이것들이 세트 아이템인지 줄줄이 딸려온다.

나는 가장 처음 외친 놈을 향해 물었다.

“네가 누군데?”

“나는 대죽산표국의 소국주…….”

“오, 죽산표국?”

“역시 아는구나!”

“몰라, 씨부럴 놈아. 죽사발 내 버리기 전에 내려.”

호북성에서는 방귀깨나 뀔지 몰라도, 내가 못 들어 봤으면 듣보잡이다.

나는 조용히 말을 이었다.

“지금 내리면 사인교만 박살 내고, 안 내리면 사인교랑 같이 네 다리도 박살낸다. 어쩔래?”

대죽산표국의 소국주가 눈을 부릅뜨며 대답했다.

“내리겠습니다.”

“진작 그럴 것이지. 그런데 눈은 왜 부릅떠?”

“죄송합니다. 안 그러면 눈물이 날 것 같아 가지고…….”

아, 그럼 인정이지.

손쉽게 한 놈을 처리한 나는 앙칼지게 외친 여자를 향해 물었다.

“어디 가문이시라고?”

“흐, 흥! 제 아무리 무뢰배라고는 하나 형문검가의 이름은 들어보았을 테지요!”

“못 들어 봤어. 개소리하지 말고 내려.”

“……!”

“자, 다음. 넌 어디냐?”

“나, 나는 응성상회의…….”

“응성인지 응가인지. 똥 지릴 때까지 맞기 싫으면 너도 내려.”

“옙.”

두세 명이 그렇게 사인교에서 내리니 남은 놈들은 말을 꺼내기도 전에 슬금슬금 땅을 밟았다.

딱 한 놈만 빼고.

“그래서, 넌 누구냐?”

얼굴에서 완전히 웃음기가 사라진 청년이 차갑게 눈을 빛냈다.

“넌 넘지 말아야 할 선을 넘었다.”

“니 생명선도 좀 넘은 것 같은데. 그래서 누구냐고.”

“허허, 별꼴을 다 겪는군.”

헛웃음을 흘린 청년이 위엄에 찬 목소리로 외쳤다.

“나, 주원공은 위대하신 황상 폐하와 팔촌 지간으로 용의 핏줄을 타고난 존귀한 몸! 네 죄를 안다면 지금이라도 무릎을 꿇어라!”

“오케이, 천룡인. 내려.”

“……!”
```

## Final English reading copy

```markdown
# Chapter 453

“You fucking baaaastards!”

For a moment, I thought a cold wind had blown through.

Or maybe my shout had simply been loud enough to feel like one.

The latter was probably more likely.

Whoooosh.

Dozens of people who had been scrambling to pick up silver nyang froze in place, and silence descended over the noisy main road.

Then, the next moment, a single sentence slipping between my lips shattered the brief quiet.

“I’m counting to three.”

“……?”

“Fall in.”

“……!”

Give a dog three years in a village school and it can recite poetry. Keep beating it for long enough and it can memorize the Four Books and Three Classics.

That was why the village-school dog—or rather, Hyuk Mujin—who had been conditioned by a year of my violence and profanity, moved faster than anyone else.

“Faaall iiiin!”

With his reply echoing like a scream, Hyuk Mujin came running and stopped right in front of me.

A beat later, Gung Gibang finally grasped what was happening and used his movement technique to arrive almost simultaneously with Hyuk Mujin. As for Cheongpung…

“Pancakes! Please give me the pancakes, quick! Benefactor is angry!”

That sibu-leol bastard. Look at him making sure to get his pancakes even now.

Once the snacks were wrapped, I spoke gently to Cheongpung as he came rushing toward me like a streak of light.

“Take your time. I’m not angry.”

“Wow! Really?”

“Yeah. I’m not angry. I’m fucking pissed.”

“Ah, ah…”

I looked at the fidgeting Cheongpung and the two others who were subtly avoiding my gaze.

*When the hell are these bastards going to become human?*

They could not even drag up the last ounce of their strength and run to the Zhuge Clan, yet look at them using martial arts to pick up a few silver nyang.

Gung Gibang had even sneakily snatched silver nyang out of someone else’s hand. At this point, he was not a beggar. He was a bandit.

*Life, for fuck’s sake…*

I had worked so hard lately for the sake of the staff’s welfare, and this was how it ended up.

I looked up at the clear sky and spat into my palm.

“Hyuk Mujin. Put your forehead here.”

“Pardon?”

Hyuk Mujin raised his head sharply and asked with an incredulous expression.

“Just me?”

“Yeah. You for now.”

“What about Young Hero Gung?”

“He’s a beggar down to his bones. Honestly, if a beggar says he’s picking up silver nyang, it’s hard to criticize him.”

“An accurate and wise judgment.”

Gung Gibang, who had been watching my mood, cut in with a solemn voice. Hyuk Mujin opened his round eyes.

“No, what do you mean, ‘hard to criticize’? You get angry every time I call you a beggar.”

“Me? What nonsense. I’m a beggar from head to toe. I was a beggar when I was born, and I’ll live as a beggar until I die.”

“……You really are a beggar.”

“Thank you for the compliment.”

“Gung Gibang, you beggar bastard.”

“Ah, how sweet.”

Hyuk Mujin glared at Gung Gibang as if he wanted to kill him, then spoke again.

“What about Young Hero Cheong?”

“Cheongpung is Cheongpung.”

Huashan Sect or not, Cheongpung was simply like that by nature.

At that one sentence, which contained everything, Hyuk Mujin muttered,

“That makes no sense, but somehow I understand…”

“There are too many people watching. Let’s finish this quickly.”

“How many?”

“Tell me. How many blows would it take for you to reflect on your actions?”

“Then… one?”

“Three.”

“Damn it. Understood.”

“You cursed, so five.”

“……Just hit me ten times. Beat me until I die.”

“I award bonus points for that determined attitude worthy of a martial artist. So one blow. How many?”

“One!”

Hyuk Mujin shouted his reply with all his might and thrust his forehead forward.

That was when it happened.

“You there. Stop.”

“……?”

I lowered my hand and turned around.

In the middle of the road, which had fallen silent enough to hear a mouse breathe, ten men and women riding in four-person sedan chairs were looking in our direction with gazes that mixed displeasure and interest.

Among them, all dressed lavishly as if to flaunt their immense wealth, one young man stood out in particular.

He was the owner of the voice I had heard moments earlier.

“I stopped. Why?”

The young man’s eyes went round at my question. He blinked for a while, as if unable to believe what he had just heard, then let out a quiet laugh.

“It seems you do not know who this Young Master is.”

“Do I have to know?”

“Have you ever seen such an arrogant bastard?”

The young man had not said that.

I looked at the man who had kicked off from the sedan chair and shot into the air.

*What is this now?*

Whoosh, clang!

After performing three somersaults in midair, the sparrow-eyed man landed and drew his sword, his eyes burning with fury.

The spectators gasped at the dazzling movement.

“You appear to be a wandering martial artist, but as if causing a disturbance in broad daylight were not enough, you dare to utter such insolent words to a person of—”

“You’ve put a lot of jewels on that. Are they meant to distract people?”

I stared at the jewels decorating his sword. Dozens of gems in a variety of colors were shining in the sunlight.

“What?”

“It’s dazzling. Put it away.”

Clang!

The sparrow-eyed man’s eyes widened.

The sword flew from his grasp when he failed to withstand the force of the finger flick I sent at him. It spun through the air and plunged deep into the ground.

“You fucking bastard. How dare you point a sword at someone so carelessly? And in broad daylight, no less.”

*Oh, look at this bastard running his mouth.*

He was probably somewhere around First Rate.

He seemed to have polished his skills to a decent level, but he was an extreme poseur obsessed with appearances.

“T-this bastard…!”

“And you were the ones making all the noise. I just made things quiet. Don’t make this more complicated than it needs to be. Just leave, all right?”

I was serious.

It was not as though this was the first time one or two flies had buzzed around me. If I was merely passing through rather than standing in front of my own home, there was no reason to spray bug killer at every mosquito that came at me.

It would be better to wave them away and continue on my way.

But no matter how sincerely you tried to explain something, there were always people who could not understand it the first time.

Shing, shing-shing!

Dozens of sword blades flashed from every direction. As martial artists from Qingxia Hall wearing blue silk martial uniforms surrounded us in layer after layer, a smug expression appeared over the sparrow-eyed man’s earlier panic.

“You appear to be a fairly well-known wandering martial artist, but even now, kneel and beg for forgiveness. Who knows? Perhaps the Young Master will show you mercy.”

I glanced over the sparrow-eyed man’s shoulder. The other men and women were watching us with bright, excited eyes, led by the young man who appeared to be their leader.

They looked exactly like spectators watching monkeys at a zoo.

“I don’t think the people over there have any intention of showing mercy.”

“What?”

“Of course, neither do I. And based on my experience so far, this is the most effective medicine. Isn’t that right?”

I slowly raised my fist, and the Bermuda Triangle, which had been watching only my expression, responded enthusiastically.

“Exactly. They won’t come to their senses until they’ve been beaten like dogs on the hottest day of summer.”

“I was the first one to take that medicine. I was cured immediately.”

“Benefactor, can I go buy some dumplings while you’re doing that?”

“No. Just stay there. It’ll be over soon anyway.”

Step.

“W-wait!”

As I took a step forward, panic filled the sparrow-eyed man’s eyes.

A Third Rate thug would charge in out of sheer stubbornness because he would not know his opponent’s level. But that man was a martial artist who had learned martial arts to a certain degree.

That was why he—and even the Qingxia Hall martial artists acting as decorative guards—had clearly realized that none of them were my match.

“W-we’re Qingxia Hall!”

“Oh. So?”

“D-did you say you’ve never heard of Qingxia Hall’s reputation?”

“Yeah. My hearing hasn’t been very good lately.”

Step.

“Stop! I said stop!”

“Ahem.”

Now the sparrow-eyed man was not the only one growing desperate.

A retainer of the Zhuge Clan, who had been watching the situation while clicking his tongue, cleared his throat and spoke.

“I will explain the situation, so perhaps it would be best if you stopped…”

Whack! Thud!

“Pardon me? What did you just say?”

“……”

The Zhuge Clan retainer looked back and forth between me, standing there with my fist clenched, and the sparrow-eyed man, who had passed out with his nose crushed.

He muttered awkwardly,

“I said it would be best if you stopped…”

“Pardon?”

“There may be various issues…”

“Pardon?”

“It would be better to avoid any unnecessary conflict…”

“What was that?”

“……Never mind.”

“Ah. Right.”

I wiped the blood from my fist on my trouser leg and looked around.

Gung Gibang was muttering that he had known that bastard would end up like this, while Hyuk Mujin’s expression was bright thanks to the extra years of life he had gained.

And Cheongpung…

“Hey! Where do you think you’re going?”

“Gasp, Benefactor!”

No way. Was that bastard actually going to buy dumplings right now…?

Seeing Cheongpung’s back as he slowly slipped away without making a sound, I began to wonder whether he was really human.

*I’m definitely catching that bastard.*

With that firm resolve, I took a step forward. The decorative guards surrounding us swallowed their breaths and moved aside.

But they were not the only Qingxia Hall martial artists present.

“Ha-ha-ha! This is amusing. Very amusing. Don’t you agree?”

At the young man’s laughing question, the four huge men carrying his four-person sedan chair answered in unison.

“Yes, my lord.”

“We cannot send off the benefactor who gave this Young Master such a good laugh. I am fine, so go and bring him here.”

“Loyalty!”

With a shout filled with internal energy, the huge men set down the sedan chair and charged toward me at a speed like the wind.

They had transformed from mere sedan bearers into outstanding Peak masters, attacking while covering all four directions.

Whoooooosh!

The moment each of their punches, infused with powerful energy, interlocked with exquisite precision and swung toward me—

Boom-boom-boom-boom!

With exactly four sounds of impact, four bodies sprawled face-first onto the ground at the same speed with which they had charged.

And they stayed down.

“What the sibu-leol?”

“……!”

“……!”

“……!”

Complete silence descended over the main road.

After lightly kicking the unconscious giants, I shrugged at the young man. The corners of his mouth, which had risen so high, were now trembling.

“Interesting. Very interesting. Don’t you all think so too?”

The Zhuge Clan retainer put a hand to his forehead, while Gung Gibang and Hyuk Mujin nodded mechanically.

“This is the most fun I’ve had in my entire thirty-year life as a beggar.”

“Captain, my belly button popped off from laughing. I can’t see where it rolled off to, so I’m still looking for it.”

“Yes, in these dry times, how could we simply send away the man who gave us such great entertainment? So…”

He pointed at the young man.

“Grab that bastard by the collar and bring him here.”

“Loyalty, loyalty!”

“I don’t know anymore. Whatever happens, you’ll handle it all yourself.”

Hyuk Mujin, who did not want to take even a single hit, burned with more enthusiasm than anyone else, while Gung Gibang stepped forward despite grumbling.

The situation had completely reversed from how it had begun.

When even the guards they had trusted were defeated, the men and women of Qingxia Hall began screaming at the tops of their lungs.

“You bastard! Do you know who I am?”

“You wretched scoundrel! Do you dare defy the laws of the Great Nation?”

“If you lay a hand on me, do you think my family will stand by and do nothing?”

I had only meant to grab one person, but these people were apparently set items that came attached in a chain.

I asked the first one who had shouted.

“Who are you?”

“I am the Young Bureau Head of the Daejuksan Escort Bureau…”

“Oh, Juksan Escort Bureau?”

“So you do know us!”

“I don’t, you sibu-leol bastard. Get down before I beat you until you’re a bowl of porridge.”

They might have thrown their weight around in Hubei Province, but if I had never heard of them, they were nobodies.

I continued quietly.

“If you get down now, I’ll only destroy the sedan chair. If you refuse, I’ll destroy your legs along with it. What’ll it be?”

The Young Bureau Head of the Daejuksan Escort Bureau widened his eyes and answered,

“I’ll get down.”

“You should have done that from the beginning. Why are your eyes so wide?”

“I’m sorry. If I don’t, I think I might cry…”

Ah. In that case, I accepted it.

After dealing with one of them easily, I turned to the sharp-voiced woman.

“What family did you say you were from?”

“Hmph! No matter how much of a scoundrel you are, surely you’ve heard of the name of the Hyungmun Sword Family!”

“Never heard of it. Stop talking nonsense and get down.”

“……!”

“Next. Where are you from?”

“I-I’m from the Eungseong Merchant Association…”

“Eungseong, Eung-poop, whatever. If you don’t want to be beaten until you shit yourself, get down too.”

“Yes, sir.”

After two or three of them climbed down from their sedan chairs, the rest began touching their feet to the ground one by one without even speaking.

All except one.

“So who are you?”

Every trace of laughter had vanished from the young man’s face. His eyes gleamed coldly.

“You have crossed a line you should never have crossed.”

“Looks like you crossed your own lifeline, too. So who are you?”

“Heh. What a ridiculous situation.”

The young man gave a hollow laugh, then shouted in a dignified voice,

“I, Ju Wongong, am a noble scion of the dragon’s blood and a third cousin of His Majesty the Emperor! If you know your crime, kneel even now!”

“Okay, Celestial Dragon.[^1] Get down.”

[^1]: The privileged world nobles in *One Piece*, infamous for treating ordinary people as beneath them.

“……!”
```
