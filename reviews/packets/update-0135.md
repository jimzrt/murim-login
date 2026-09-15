<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0135.txt",
      "sha256": "ac141ea5a7a5b25de6e661ad899642ab45e5798d4f20c82bcfb5540eb9583284",
      "bytes": 14245
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "2655ed899a0b9c1d4d2240c26a1381b4297fe1dda16daa3a871c01106023209f",
      "bytes": 8083
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c84177b336ceb467ef1e867776bf1deeff25175fce5f6a0b398fb33bfa07b62d",
      "bytes": 26786
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "687b4e27fbfd9fe72ea7360c30b0368d5ad532565817fcf66bc24d4b71cca85c",
      "bytes": 755
    },
    {
      "path": "characters/Childeuk.md",
      "sha256": "98a440735c4ab53723d5484cb9811816703dbb6ec004a8b34c98927378f8842a",
      "bytes": 652
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "e9603fb587987c9c905d8e7fe56beb863e72ca5102653e0d211c661317d74bb5",
      "bytes": 5353
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "5a916c66439085a18505ed08771320e1222262cd7fcb88061f2e9c4ae3f95018",
      "bytes": 1511
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "6c6101e0ce22966ce77b589a4142bb138835a99bce14a74b4de5c3dc6c5ea1ba",
      "bytes": 622
    },
    {
      "path": "characters/Woo Jintae.md",
      "sha256": "50ce9fbb06519fe52db8f824cc93da03e169c36c279a1f60a0b7362a9cea7112",
      "bytes": 805
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "b81fcf0b3e6de424aabe9cf1789cea94522c7d9794ada0cb6f08a2c1ac7fe071",
      "bytes": 22414
    }
  ],
  "estimated_tokens": 24238
}
-->

# Durable State Update — Chapter 135

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 135. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 135. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Speaker and addressee must be Hangul source spellings (Arabic digits
allowed in titles such as 1팀장; do not romanize). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 135,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 135,
    "continuity_sources": [135],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "speaker Korean",
      "addressee": "addressee Korean",
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

## Prior durable context

```json
{
  "active_continuity": [
    "Pung Yang is dead; Jin Taekyung killed him after the Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed his Body-Protecting Qi and pierced his chest.",
    "Taekyung fully absorbed the Blazing Flame Divine Pill and possesses forty-five years of internal energy with the Scorching Yang Qi attribute.",
    "Jin Mukyung survived his fight with Pung Yang and returned to the Jin Family of Taiyuan, but remains incompletely recovered.",
    "Cheol Mubaek remains severely injured and needs extended recuperation; Lee Seowol remains the seventeen-year-old Sect Leader of the Mount Heng Sword Sect and vows to preserve it.",
    "The Lower District Sect sent a relief force after the battle; Wolhwa's real name is Eun Sowol, and she is its Shanxi Branch Leader.",
    "Lee Seowol accepted the Jin Family of Taiyuan's New Year invitation, offered the Mount Heng Sword Sect's territorial rights as an apology, and proposed marriage to Taekyung in exchange for three Peak martial arts; Taekyung plans to reject her because of her age and because he loves Song Song.",
    "Forty-seven mounted bandits survived the battle, but the Lower District Sect can save only about thirty; it is spreading a rumor that the two Jin brothers defeated Pung Yang and rescued Mount Heng.",
    "Cheol Mubaek and Lee Cheonbaek became close friends after first meeting and fighting more than thirty years ago; Cheol is the ninth-generation successor of the Shura Annihilating Fist.",
    "Jopil is dead and left behind the Supreme Peak martial art Flame Divine Palm; the Fire King and the status of the Fire Gate Clan's single successor remain unknown.",
    "The Temporary Strength Pill is in Taekyung's Inventory and has been revealed to Jin Wikyung, Jin Mukyung, and Wipeng; its System description identifies Dark Heaven as its manufacturer and records its unknown Grade, Peak restriction, temporary power increase, +100 combat stats, fifteen years of internal energy, and Body-Protecting Qi effect.",
    "Jin Wikyung and Wipeng traveled to Sakju with fifty elite guards after receiving an emergency report about Pung Yang, the Red Wind Band, the Mount Heng Sword Sect, and the Jin brothers; the Jin Family displayed a large Sakju banner celebrating the safe return of Mukyung, Taekyung, and Hyuk Mujin.",
    "Taekyung, Mukyung, Wikyung, and Wipeng drank through the night for three days; Wipeng is called the God of Drinking and Taekyung is rumored to be the Night King.",
    "Taekyung's Sleeping Dragon of Shanxi Title effect strengthened to all stats +15 and Fame +200; his current Status Window shows Level 61, Fame 2,100 (+250), and 60 remaining points.",
    "Hyuk Mujin accepted The City Lord's Invitation, requiring attendance at the City Lord's luncheon with young prodigies tomorrow.",
    "The City Lord of Shanxi Province is a ten-year-old Prince and the Emperor's youngest brother, appointed at age five; Jin Mukyung met him after being summoned three years earlier and considered the encounter a nightmare.",
    "Cheongpung is an eccentric former porter who recently fled Huashan's Lotus Peak and traveled toward Taiyuan; he is an exceptionally young Peak master whose Level Taekyung cannot determine through Qi Sense, lived with his grandfather in the mountains from age five, and came down to test himself against the Ten Dragons and Phoenixes.",
    "Hyuk Mujin's parents are healthy textile merchants in Taiyuan who own the city's largest textile shop, with branches in Henan and Hebei; Mujin left home to avoid inheriting the business, and a younger sibling later removed that obligation.",
    "Taekyung has begun treating Hyuk Mujin as a valued companion rather than merely a subordinate, acknowledging the hardship Mujin endured while traveling with him.",
    "Woo Jintae is the married, nearly thirty-year-old heir and sole male heir in three generations of the Seongun Escort Bureau; he cultivates the current Five Gates scions through lavish hospitality, gifts, and bribes.",
    "At Honghwa Inn, Taekyung repeatedly slapped Woo Jintae after Jintae refused to apologize; the other Five Gates scions apologized to Cheongpung after Mujin's intervention, and Mujin then ordered them to prostrate themselves."
  ],
  "continuity_sources": [
    134,
    133
  ],
  "open_questions": [
    "How will the Jin Family of Taiyuan respond to Lee Seowol's proposed transaction and territorial transfer?",
    "Can Lee Seowol preserve or rebuild the Mount Heng Sword Sect with so few survivors?",
    "What are the Temporary Strength Pill's exact price and long-term aftereffect, and is it related to the Demonic Cult's Blood-Exploding Pill?",
    "What is Dark Heaven, and why do Jin Wikyung and Wipeng refuse to discuss it?",
    "What consequences will Pung Yang's death have for the Red Wind Band and the wider Murim?",
    "Is the Fire King still alive, and if so, where is he?",
    "Will the Five Gates scions obey Hyuk Mujin's order, and what will happen at the City Lord's luncheon?",
    "What was Cheongpung's status at Huashan's Lotus Peak, who is his grandfather, and what are the individual sect affiliations or family names of the Five Gates scions, including the Wang Family Estate heir and Young Lady Shin?"
  ],
  "safe_through": 134,
  "temporary_decisions": [
    "Render 잠력단 as Temporary Strength Pill and 폭혈단 as Blood-Exploding Pill.",
    "Render 만년한철 as Ten-Thousand-Year Cold Iron and 이름 없는 검 as Unnamed Sword.",
    "Render 열화신단 as Blazing Flame Divine Pill and 반 갑자 as half a jiazi, clarified as thirty years of internal energy.",
    "Render 완전 회복 as Full Recovery and 회광반조 as final rally in this death-and-recovery context.",
    "Render 운칠기삼 as seven parts luck and three parts skill, and 운구기일 as nine parts luck and one part qi, with a footnote explaining the variation.",
    "Render 은공 as Benefactor, 절정 무공 as Peak martial arts, 급식 as school lunch, 고딩 as high schooler, 철컹 as clank, 산서성 as Shanxi Province, 총지부장 as Chief Branch Leader, 원단 as New Year's Day, 갑자 as jiazi, 시진 as shichen, 표행 as escort run, 쟁자수 as porter, 표국 as Escort Bureau, 표두 as Escort Chief, 은원보 as silver ingot, 은자 as nyang of silver, 사서삼경 as the Four Books and Three Classics, and 연화봉 as Lotus Peak.",
    "Render 일인전승 as single successor, 비인부전 as transmission only to the worthy, 구 대 계승자 as ninth-generation successor, 천하십대권법 as the ten greatest fist techniques in the world, 열화문 as Fire Gate Clan, 화왕 as Fire King, 삼성 as Three Saints, 십왕 as Ten Kings, 진무보법 as Jin Family's Manoeuvre Technique, 아이템창 as Item Window, 전서응 as messenger eagle, 고원 as Gaoyuan, 구주 as Nine Provinces, 사술 as dark arts, 마기 as demonic qi, 선천지기 as innate qi, 소음인 as Soeumin, 태양인 as Taeyangin, 암천 as Dark Heaven, 주신 as God of Drinking, 야왕 as Night King, 화주 as fire liquor, 화북 as North China, 현령 as county magistrate, 성주 as City Lord, 장 노인 as Old Man Jang, 적토마 as Red Hare, 여포 as Lü Bu, 성주의 초청 as The City Lord's Invitation, 친왕 as Prince, 주씨 as Zhu, 천자 as Son of Heaven, 황상 and 황제 as Emperor, 태자 as Crown Prince, 구파일방 as Nine Sects and One Gang, 오대세가 as Five Great Families; render 개방 as Beggars' Sect and 십봉룡 as Ten Dragons and Phoenixes.",
    "Render 빙당호로 as candied hawthorn skewers with an explanatory footnote; render 산니백육 as Garlic Pork, 어향육사 as Fish-Fragrant Shredded Pork, 경장육사 as Beijing Sauce Shredded Pork, 규화계 as Beggar's Chicken, 매구 as Maegu, 매채구육 as Maechae Guyuk with a footnote explaining the abbreviation, 촉금 as Shu brocade, 삼도문 as Samdo Sect, and 궁귀문 as Gunggui Sect.",
    "Render 도동파 as Dodong Sect and 천진반 as Tien Shinhan, preserving Taekyung's fabricated identity joke."
  ],
  "version": 1
}
```

## Existing names ledger

# Established Names

Binding Korean → English for names, titles, aliases, and forms established in
accepted chapters. Injected only when the exact Korean appears in the current
chapter. Overrides `compendium.md` on the same Korean key. Add a row at first
use. First use of an unlisted name or title almost always needs a footnote.

| Korean | Preferred English | Notes |
| ------ | ----------------- | ----- |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 녹림십팔채 | **Eighteen Strongholds of Green Forest** | |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 산음 | **Saneum** | Jin Family branch location |
| 삭주 | **Sakju** | Jin Family branch location |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |
| 견정 | **Gyeonjeong** | Acupoint |
| 아문 | **Amun** | Acupoint |
| 봉안 | **Bongan** | Acupoint |
| 입동 | **Ip-dong** | Acupoint |
| 갱생권 | **Reformation Fist** | Jin Mukyung's named fist technique |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 공청석유 | **gongcheong seokyu** | Rare martial-arts elixir; the term also creates a petroleum pun. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 삼문협 | **Three Questions Gorge** | A distant gorge and route connecting Shanxi with Shaanxi and Henan. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 약왕당주 | **Medicine King Hall Master** | The unnamed physician who runs the Medicine King Hall. |
| 송검문 | **Song Sword Sect** | Small-to-medium sect in central Shanxi. |
| 송검문주 | **Sect Leader of Song Sword Sect** | Title held by Huang. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 황 모 | **Huang** | Surname-style self-reference by the Sect Leader of Song Sword Sect. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 낙류검 | **Falling Flow Sword** | Named sword technique discovered by Mukyung in the archives of Heaven's Gate Temple; its name evokes a waterfall. |
| 질풍십이권 | **Twelve Gale Fists** | Named fist technique Mukyung threatens to use against Taekyung. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 분근착골 | **Tendon-Splitting and Bone-Twisting** | Cruel immobilization technique described by Mukyung. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 군자검 | **Junzi Sword** | Epithet Jin Wikyung begins receiving after the war. |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 천자문 | **Thousand Character Classic** | Classical text Childeuk cannot complete. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 최 팀장 | **Team Leader Choi** | Team Leader who owns the café where Taekyung signs a contract. |
| 명품충 | **Designer-Brand Junkie** | Display name used by Team Leader Choi in a text message. |
| 평화 | **Peace Guild** | Guild name. |
| 김 집사 | **Butler Kim** | Choi's butler and limousine driver. |
| 히말라야 | **Himalayas** | Mountain region referenced as the source of the bottled water. |
| 히말라야의 정수 | **Essence of the Himalayas** | System-named consumable that temporarily raises Intelligence. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 강남 | **Gangnam** | Formerly valuable Seoul-area real estate. |
| 분당 | **Bundang** | Formerly valuable Korean real estate area. |
| 대한민국 | **Korea** | Country reference. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 순이네 수퍼 | **Sooni's Super** | The Peace Guild's Guild house. |
| 송 양 | **Miss Song** | The Peace Guild's final member; full identity not yet given. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 논산 | **Nonsan** | Location of Korea's Hunter training center. |
| 임혁준 | **Im Hyeokjun** | Im Kkeokjeong's personal name, shown in the System Level window. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 부천터미널 길드 | **Bucheon Terminal Guild** | Guild whose raid footage is shown. |
| 미노타우로스의 미로 | **The Minotaur's Labyrinth** | B-rank Gate. |
| 상동 길드 | **Sangdong Guild** | Mid-sized Guild near Bucheon that joins Peace Guild's first official raid. |
| 헌터 협회 | **Hunter Association** | Organization investigating the Bucheon Terminal Guild fatality. |
| 흑색 드레이크 | **Black Drake** | B-rank monster whose leather and spine are used for Taekyung's loaned equipment. |
| 장인의 흑색 드레이크 가죽 세트 | **Masterwork Black Drake Leather Set** | Peak-grade armor set loaned to Taekyung. |
| 장인의 검은 가시 창 | **Masterwork Black Thorn Spear** | Peak-grade spear loaned to Taekyung. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 니콜라스 | **Nicholas** | North American craftsman associated with the space-expansion suitcase. |
| K사 | **K Company** | Manufacturer of the space-expansion suitcase. |
| 혜린 | **Hye-rin** | C-rank female mage and member of Im Changsoo's Sangdong Guild team. |
| 청담동 | **Cheongdam-dong** | District mentioned as a luxury shopping location. |
| 투우사의 전신 갑옷 | **Matador’s Full-Body Armor** | Peak-grade armor equipped by Im Kkeokjeong; grants bonuses against bovine-type monsters. |
| 투우사의 방패 | **Matador’s Shield** | Peak-grade shield equipped by Im Kkeokjeong; can activate Taunt and Hallucination against bovine-type monsters. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 환각 | **Hallucination** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 미노타우로스 전사 | **Minotaur Warrior** | Level-window designation for the first Minotaur encountered in the labyrinth. |
| 발설지옥 | **tongue-pulling hell** | Buddhist hell associated with punishment for liars and slanderers; explained in a footnote. |
| 껄떡쇠 | **Horndog** | Im Changsoo’s nickname for his womanizing. |
| 강원도 | **Gangwon Province** | Province named in Taekyung’s joke about the Minotaur’s next life. |
| 횡성 | **Hoengseong** | Place in Gangwon Province named in Taekyung’s joke. |
| 자일리톤 | **Xyliton** | Finnish equipment manufacturer whose custom helmet records video. |
| 유네스코 | **UNESCO** | Organization referenced in Taekyung’s cultural-heritage joke. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 미노타우로스 대전사 | **Minotaur Warrior** | Level 70 B-rank boss monster of The Minotaur's Labyrinth. |
| 임 팀장님 | **Team Leader Im** | Formal address for Im Changsoo used by a Sangdong Guild teammate. |
| 프로즌 | **Frozen** | Im Chunsoo's epithet as an A-rank ice mage. |
| K은행 | **K Bank** | Bank where Im Changsoo's transfer is reported. |
| 김정희 | **Kim Jeonghee** | Jin Taekyung and Hayeon's mother; restaurant kitchen worker |
| 아줌마 | **ajumma** | Familiar term for a middle-aged or married woman, used for Kim Jeonghee |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 김민수 | **Kim Minsu** | The restaurant owner's son; D-rank Hunter in Sangdong Guild. |
| 민수 | **Minsu** | Short form used for Kim Minsu. |
| 운기요상 | **Circulate Qi for Healing** | System-named skill that channels internal energy through another person's body to cleanse accumulated waste and restore health. |
| 하급 포션 | **Lesser Potion** | Low-grade healing potion issued as raid supplies; its System Grade is Third Rate. |
| 3차 각성자 | **third-awakening Hunter** | Hypothetical Hunter classification that would come after reawakening. |
| 재각성 | **reawakening** | Established Hunter awakening category described as having no further stage. |
| 피의 일주일 | **Bloody Week** | The hellish first week after Gates opened, during which casualties reached the tens of millions. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 박지훈 | **Park Jihoon** | Current name of Taekyung's former middle-school classmate; Hunter in Myeongdong Guild Team 1. |
| 박지황 | **Park Jihwang** | Jihoon's former name, revealed when Taekyung recognizes him. |
| 가람중 | **Garam Middle School** | Middle school attended by Taekyung and Jihoon. |
| 명동 길드 | **Myeongdong Guild** | Large Guild in which Jihoon belongs to Team 1. |
| 1팀장 | **Team 1 Leader** | Sangdong Guild's Team 1 leader and its only A-rank Hunter besides Im Chunsoo. |
| 희망 고시원 | **Hope Goshiwon** | The goshiwon listed as Taekyung's residence in the target report. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 집파리 | **Housefly** | System label for a Level 1 fly familiar. |
| 검정파리 | **Black Blow Fly** | System label for a Level 1 fly familiar. |
| 금파리 | **Green Bottle Fly** | System label for a Level 1 fly familiar. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 김선희 | **Kim Seonhee** | Assistant Manager at the Ilsan Store |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 라페스타 | **Lafesta** | Shopping and entertainment district in Ilsan |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 쌀벌레 | **Rice Weevil** | Creature used by Hong Woojin as a Familiar |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 김희선 | **Kim Seonhee** | Source spelling variant for the established Assistant Manager Kim Seonhee at the Ilsan Store. |
| 여름이 | **Yeoreum** | Name Hayeon gives to the Level 2 kitten. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 고양시 | **Goyang** | City where the target previously visited a real-estate office. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 최병일 | **Choi Byungil** | B-rank Security Team leader; his Level is in the mid-sixties. |
| 박형진 | **Park Hyungjin** | One of the C-rank Sangdong Guild watchers. |
| 오규현 | **Oh Gyuhyeon** | One of the C-rank Sangdong Guild watchers. |
| 이민철 | **Lee Mincheol** | One of the C-rank Sangdong Guild watchers. |
| 교관 | **Instructor** | Kim Hwajong's former Hunter Training Center role and address. |
| 헌터 훈련소 | **Hunter Training Center** | Training institution where Kim Hwajong served as an instructor. |
| 1번 훈련생 | **Trainee Number One** | Im Chunsoo's training call sign during his forced military identification. |
| 28연대 1대대 2중대 | **28th Regiment, First Battalion, Second Company** | Military unit designation shouted during Im Chunsoo's identification. |
| 사도세자 | **Crown Prince Sado** | Joseon crown prince used in the comparison for Jinho's haggard appearance; footnoted. |
| 박혁거세 | **Park Hyeokgeose** | Legendary founder of Silla, used in the comparison to Jinho emerging from the capsule; footnoted. |
| 열양공 | **heat-yang technique** | Mukyung's heat-based internal-energy technique. |
| 옥황상제 | **Jade Emperor** | Daoist deity invoked in Hyuk Mujin's prayer. |
| 원시천존 | **Primordial Heavenly Venerable** | Daoist deity invoked alongside the Jade Emperor. |
| 항산검문주 | **Sect Leader of the Mount Heng Sword Sect** | Title for Lee Seowol, the sect's current leader. |
| 산서제일미 | **Shanxi's foremost beauty** | Former reputation of Taekyung's mother. |
| 봉황객잔 | **Phoenix Inn** | Famous Shanxi inn with luxurious lodging, imperial-court cuisine, and a beautiful proprietress. |
| 계용옥미갱 | **chicken-and-corn soup** | Egg-thickened corn soup. |
| 계용옥미앵 | **chicken-and-corn soup** | Source spelling variant of 계용옥미갱 for the same dish. |
| 광수 | **Gwangsu** | First attacker at the Phoenix Inn; identified by the others after Taekyung punches him. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 관제묘 | **Guandi Temple** | Shrine type mentioned in martial-arts novels. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 오색귀 | **Five-Colored Ghosts** | Nickname for the five former subordinates of Jang Sam. |
| 이삼 | **Lee Sam** | Leader of the ten-man human-trafficking group; his Level window identifies him by this name. |
| 추종향 | **tracking scent** | Scent used to guide the messenger hawk. |
| 대동 | **Datong** | Shanxi location containing the Mount Heng Sword Sect branch destroyed by the Red Wind Band. |
| 토호단 | **Earth Tiger Band** | Mounted-bandit group formerly led by Pung Yang's subordinate. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 춘삼 | **Chunsam** | Lower District Sect martial artist serving as the carriage driver. |
| 철검대주 | **Iron Sword Squad Leader** | Title of the Mount Heng Sword Sect's Iron Sword Squad leader. |
| 대항산검문 | **great Mount Heng Sword Sect** | Expanded organizational form used for the Mount Heng Sword Sect. |
| 대동지부 | **Datong Branch** | Mount Heng Sword Sect branch in Datong. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 철 숙부 | **Uncle Cheol** | Lee Seowol's familial address for Cheol Mubaek. |
| 철 대협 | **Great Hero Cheol** | Respectful address for Cheol Mubaek. |
| 아가씨 | **Young Lady** | Former address used for Lee Seowol before she demands the title Sect Leader. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 산서괴협 | **Strange Hero of Shanxi** | Epithet referenced for the absent martial artist. |
| 녹림맹주 | **Green Forest Alliance Leader** | Leader title for the Green Forest Alliance. |
| 장강수로맹주 | **Alliance Leader of the Yangtze River Channel League** | Leader title for the Yangtze River Channel League. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 절정 초입 | **early Peak** | Pung Yang's specific stage within the Peak realm. |
| 광칠이 | **Gwangchil** | Former mounted-bandit boss who took in Pung Yang and was later killed by a First Rate master. |
| 일류 초입 | **early First Rate** | Early stage of the First Rate realm. |
| 수라멸권 | **Shura Annihilating Fist** | Cheol Mubaek's single-successor martial art. |
| 항산권문 | **Mount Heng Fist Sect** | Alternate fist-sect designation used by Pung Yang for the Mount Heng defenders. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 적혈십이검 | **Crimson Blood Twelve Swords** | Peak-level martial arts manual discovered by Pung Yang. |
| 적혈심법 | **Crimson Blood Cultivation Technique** | Cultivation technique discovered by Pung Yang. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 태산압정 | **Mount Tai Presses Down on the Crown** | First move of the Three Calamities Sword Technique. |
| 나려타곤 | **Narye tagon** | Humiliating idiom comparing a fighter's evasive roll to a lazy donkey rolling on the ground. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 격산타우 | **Striking the Ox Across the Mountain** | Palm technique that transmits force through an intervening defense. |
| 북망산 | **Mount Beimang** | Mountain associated with burial grounds; used as a threat to send someone to their death. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 적혈십이도 | **Crimson Blood Twelve Sabers** | Pung Yang's domineering saber art; he has reached approximately seventy percent mastery. |
| 영단 흡수 | **Divine Pill Absorption** | System Quest created after Jin Taekyung takes the Blazing Flame Divine Pill. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 이름 없는 검 | **Unnamed Sword** | Oldest inventory item summoned when no item named 아무거나 can be found. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 완전 회복 | **Full Recovery** | Immediate Quest success reward that heals Taekyung's injuries. |
| 뛰어난 금창약 | **Superior Wound Medicine** | Quest reward used to treat external injuries. |
| 십년하수오 | **Ten-Year He Shouwu** | Quest reward used to treat internal injuries. |
| 어제의 적, 오늘의 동지 | **Yesterday's Enemy, Today's Ally** | Quest completed when Taekyung delivers Wikyung's invitation. |
| 회광반조 | **final rally** | Terminal burst of apparent vitality before death. |
| 운칠기삼 | **seven parts luck and three parts skill** | Established Korean saying used in Taekyung's reflection. |
| 운구기일 | **nine parts luck and one part qi** | Taekyung's playful variation on 운칠기삼. |
| 혈랑검법 | **Blood Wolf Sword Technique** | Peak sword technique personally created by Lee Cheonbaek. |
| 혈랑보법 | **Blood Wolf Footwork** | Peak footwork technique personally created by Lee Cheonbaek. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 정양지부장 | **Jeongyang Branch Leader** | Leader of the Lower District Sect's Jeongyang Branch. |
| 혼주지부장 | **Honju Branch Leader** | Leader of the Lower District Sect's Honju Branch. |
| 총지부장 | **Chief Branch Leader** | Title Wolhwa holds within the Lower District Sect. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 진무보법 | **Jin Family's Manoeuvre Technique** | Named Jin Family footwork technique mastered by Taekyung. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 폭혈단 | **Blood-Exploding Pill** | Demonic Cult pill said to kill the user after its time limit. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 산서제일인 | **Shanxi's Number One** | Jin Wikyung's reputation for physical strength. |
| 금잔디 | **Geum Jandi** | Heroine of Boys Over Flowers, referenced in a sarcastic comparison. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 소음인 | **Soeumin** | One of the constitutional types in Sasang medicine. |
| 태양인 | **Taeyangin** | One of the constitutional types in Sasang medicine. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 화북 | **North China** | Regional designation used when discussing Shanxi drinking culture. |
| 산서제일가 | **foremost family in Shanxi** | Description of the Jin Family of Taiyuan's standing. |
| 장 노인 | **Old Man Jang** | Elderly villager who witnesses the Jin Family's arrival. |
| 현령 | **county magistrate** | County official who greets Jin Taekyung and delivers the City Lord's invitation. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 적토마 | **Red Hare** | Famous horse used in Hyuk Mujin's exaggerated comparison. |
| 여포 | **Lü Bu** | Historical warrior used in Hyuk Mujin's exaggerated comparison. |
| 성주의 초청 | **The City Lord's Invitation** | System Quest title. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 주씨 | **Zhu** | Surname of the imperial ruling house. |
| 친왕 | **Prince** | Imperial title held by the Shanxi City Lord. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 석칠 | **Seokchil** | Middle-aged porter with nearly twenty years of experience. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 송 표두 | **Escort Chief Song** | Unnamed person responsible for the escort run. |
| 연화봉 | **Lotus Peak** | Peak on Huashan from which Cheongpung recently fled. |
| 빙당호로 | **candied hawthorn skewers** | Traditional fruit skewers coated in hardened sugar; explained in a footnote. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 혁가 포목점 | **Hyuk Family Textile Shop** | Taiyuan textile shop owned by Hyuk Mujin's parents; the largest in Taiyuan, with branches in Henan and Hebei. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |
| 메구미 | **Megumi** | Japanese name used in Taekyung's joke about the abbreviated dish name. |
| 산니백육 | **Garlic Pork** | Boiled pork sliced thin and served with garlic sauce. |
| 어향육사 | **Fish-Fragrant Shredded Pork** | Shredded pork dish. |
| 경장육사 | **Beijing Sauce Shredded Pork** | Shredded pork dish. |
| 규화계 | **Beggar's Chicken** | Named inn dish. |
| 매구 | **Maegu** | Waiter's shortened name for Maechae Guyuk. |
| 매채구육 | **Maechae Guyuk** | Pork belly with preserved mustard greens; the abbreviation is explained in a footnote. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 우진태 | **Woo Jintae** | Heir of the Seongun Escort Bureau and host of the Five Gates scions. |
| 우 소협 | **Young Hero Woo** | Honorific address for Woo Jintae. |
| 황 소저 | **Young Lady Hwang** | Honorific address for an unidentified young woman who is the only daughter of a martial sect. |
| 혁 아우 | **Little Brother Hyuk** | Familiar address for an otherwise unnamed male scion who calls Woo Jintae hyung. |
| 국주님 | **Chief** | Honorific title for the head of an Escort Bureau. |
| 촉금 | **Shu brocade** | Fine brocade brought from Sichuan. |
| 삼도문 | **Samdo Sect** | One of the five former Five Gates sects annihilated at Eight Spring Gorge. |
| 궁귀문 | **Gunggui Sect** | One of the five former Five Gates sects annihilated at Eight Spring Gorge. |
| 성룡이 | **Seongryong** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 명화 | **Myeonghwa** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 소혜 | **Sohye** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 도동파 | **Dodong Sect** | Fabricated sect claimed by Taekyung when Woo Jintae demands his affiliation. |
| 천진반 | **Tien Shinhan** | Fabricated personal identity claimed by Taekyung. |
| 왕가장 | **Wang Family Estate** | Family estate whose heir is one of the Five Gates scions; he uses sabers rather than sword arts. |
| 왕 공자 | **Young Master Wang** | Heir of the Wang Family Estate. |
| 신 소저 | **Young Lady Shin** | Young woman described as the only daughter of a martial sect. |

## Existing address-pair ledger

# Established Address Pairs

Exceptional speaker → addressee forms established in accepted chapters.
Injected only when both endpoints are present in the current chapter: the
Korean appears in the source, or belongs to a matched compact profile.
Overrides generic relationship prose in character profiles for this pair.

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진태경 | 성진호 | junior_to_older_friend | Jinho hyung | casual-but-junior | Retain hyung for 형; Jinho is three years older. |
| 성진호 | 진태경 | older_friend | informal / younger-brother | teasing-senior | Speaks informally while demanding respect as the older friend. |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 공야청 | junior_to_respected_hero | Great Hero Gong | deferential | Taekyung consistently attaches 대협 when addressing Gong Yacheong. |
| 위팽 | 송검문주 | visitor_to_sect_leader | Sect Leader | formal-polite | Wipeng addresses the Song Sword Sect Leader respectfully while delivering the summons. |
| 송검문주 | 위팽 | sect_leader_to_visiting_master | Great Hero Wipeng | deferential | The Sect Leader addresses Wipeng as 위 대협 while fearing the Ghost Sword's power. |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 칠득이 | 진위경 | servant_to_lesser_family_head | Lesser Family Head | deferential | Childeuk repeatedly addresses Wikyung as 소가주님. |
| 진위경 | 칠득이 | lesser_family_head_to_servant | you | formal-but-familiar | Wikyung addresses Childeuk with 자네. |
| 진위경 | 장칠득 | lesser_family_head_to_direct_martial_artist | Martial Artist Jang | affectionate and ceremonious | Wikyung embraces and exuberantly praises Childeuk after acknowledging their minor misunderstanding. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 최 팀장 | guild_member_to_team_leader | Team Leader | deferential | Taekyung addresses Choi as 팀장님. |
| 최 팀장 | 진태경 | team_leader_to_guild_member | Taekyung | formal-but-familiar | Choi addresses him as 태경 씨. |
| 진태경 | 김 집사 | client_to_butler | Butler Kim | formal-deferential | Taekyung addresses him as 김 집사님. |
| 최 팀장 | 김 집사 | employer_to_butler | Butler Kim | formal-polite | Choi addresses him as 김 집사님. |
| 김 집사 | 진태경 | butler_to_hunter_client | Hunter | deferential | Butler Kim refers to Taekyung as 헌터님. |
| 임꺽정 | 송 양 | older_guild_member_to_younger_female_guild_member | Miss Song | hearty-casual | Im Kkeokjeong calls her 송 양. |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 진태경 | 김 집사 | junior_to_senior_Hunter | Senior | deferential | After learning that Butler Kim trained at the same Nonsan regiment and battalion, Taekyung addresses him as 선배님. |
| 김 집사 | 최 팀장 | butler_to_employer | Young Master | deferential | Butler Kim addresses Choi as 도련님 when agreeing to follow his decision about Guild titles. |
| 임창수 | 혜린 | sponsor_to_sponsored_lover | Hye-rin | condescending-casual | Changsoo refers to himself as this oppa while claiming he will protect her. |
| 최 팀장 | 임꺽정 | guild_team_leader_to_guild_member | Hunter Im | formal-polite | Choi addresses Kkeokjeong as 임 헌터님 while telling him to put on the equipment. |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |
| 임창수 | 송송이 | rival_guild_team_leader_to_guild_member | Miss Song | mock-polite | Uses 송송이 씨 while proposing that Song Song join Sangdong Guild. |
| 송송이 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo—no, Im Changsoo | blunt but polite | Insults Changsoo with 씹창 and then corrects herself to his proper name while rejecting him. |
| 송송이 | 김 집사 | guild_member_to_guild_master | Guild Master | formal-polite | Requests the Guild Master’s permission before changing Guilds under the wager. |
| 송송이 | 최 팀장 | guild_member_to_team_leader | Team Leader | formal-polite | Asks Choi whether he accepts her possible Guild transfer if the bet is lost. |
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 김 집사 | 임창수 | guild_master_to_rival_guild_member | Changsoo | mock-polite | Butler Kim uses 창수 씨 while accusing Changsoo of refusing to pay. |
| 지점장 | 임춘수 | bank_branch_manager_to_guild_master | Guild Master | formal-deferential | The K Bank branch manager addresses Im Chunsoo as 길드장님 while reporting Changsoo's transfer. |
| 임춘수 | 임창수 | father_to_son | Changsoo | furious-parental | Im Chunsoo uses Changsoo's name alongside hostile forms such as that bastard and you little shit. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 김정희 | 사장님 | employee_to_restaurant_owner | Boss | formal-polite, becoming firm | Uses the owner's title while demanding an apology and defending Taekyung. |
| 사장님 | 김정희 | restaurant_owner_to_employee | Ajumma | condescending-casual | Repeatedly uses 아줌마 while berating Kim Jeonghee. |
| 진태경 | 김정희 | son_to_mother | Mom | casual-familiar and affectionate | Taekyung's first words after entering the restaurant and seeing his mother. |
| 김정희 | 진태경 | mother_to_son | Son | affectionate-familiar | Calls Taekyung 아들 when surprised by his visit and later asks whether he has eaten. |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 부동산 아저씨 | 진태경 | real_estate_agent_to_customer | Boss | polite and sales-friendly | The unnamed real estate agent repeatedly addresses Taekyung as 사장님 while arranging a house viewing. |
| 여자 친구 | 박지훈 | girlfriend_to_boyfriend | Oppa | casual-familiar | Jihoon's girlfriend addresses him as 오빠 while asking him to return to the car. |
| 임춘수 | 1팀장 | guild_master_to_team_leader | Team 1 Leader | blunt-commanding | Chunsoo addresses him with a rough 야 while issuing orders and demanding his candid assessment. |
| 1팀장 | 임춘수 | guild_team_leader_to_guild_master | Guild Master | formal-deferential | The Team 1 Leader consistently addresses Chunsoo as 길드장님 while reporting and accepting orders. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 동료 | 김준수 | Security Team colleague | Junsu | casual-collegial | Uses 준수야 while checking whether Junsu pulled an all-nighter. |
| 보안팀장 | 김준수 | team_leader_to_subordinate | Kim Junsu | blunt-commanding | Shouts 김준수 when the target begins moving. |
| 김권동 | 보안팀장 | subordinate_to_team_leader | Team Leader | deferential | Uses 팀장님 over the radio while reporting on the disguised approach. |
| 보안팀장 | 1번 | supervisor_to_surveillance_agent | Number One | command-radio | Uses the operative’s radio call sign while directing the real-estate-office surveillance. |
| 보안팀장 | 2번 | supervisor_to_surveillance_agent | Number Two | command-radio | Uses the operative’s radio call sign while ordering continued observation. |
| 부동산 아줌마 | 진태경 | real_estate_agent_to_customer | Boss; young bachelor | chatty-polite and flirtatious | The agent calls Taekyung 사장님 and 총각 while offering listings and commenting on his appearance. |
| 김권동 | 진태경 | surveillance_hunter_to_target | young man | friendly and polite | Gwondong maintains his ordinary-neighbor disguise and addresses Taekyung as a younger local acquaintance. |
| 진하연 | 여름이 | caretaker_to_kitten | Yeoreum | affectionate-casual | Hayeon repeatedly calls the kitten by name and refers to herself as Sis. |
| 김권동 | 김준수 | Security Team colleagues | Junsu | casual-collegial | Gwondong uses 진수야 while questioning Junsu’s interpretation of the item. |
| 보안팀장 | 김권동 | team_leader_to_subordinate | Gwondong | blunt-commanding | Uses 권동아 while directing the operation. |
| 진태경 | 최병일 | target_to_attacking_team_leader | Mr. Choi Byungil | mock-polite and taunting | Uses 최병일 씨 while baiting and confronting him. |
| 진태경 | 김준수 | target_to_surveillance mage | Junsu | casual and taunting | Uses 준수야 while questioning him. |
| 임춘수 | 진태경 | guild_master_to_younger_rival | you | blunt-but-familiar | Repeatedly uses 자네 while challenging and testing Taekyung. |
| 김화종 | 임춘수 | familiar_mage_to_guild_master | Chunsoo | gentle-and-familiar | Addresses Im Chunsoo as 춘수 on arriving at the hiking-trail entrance. |
| 임춘수 | 김화종 | former_trainee_to_former_instructor | Instructor | deferential and fearful | Im Chunsoo addresses Hwajong as 교관님 after recognizing his former instructor. |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 1팀장 | 보안팀장 | guild_team_leader_to_security_team_leader | Security Team Leader | formal-commanding | Team Leader 1 directly addresses the Security Team Leader while warning him about discipline. |
| 보안팀장 | 1팀장 | security_team_leader_to_guild_team_leader | Team Leader 1 | formal-deferential | The Security Team Leader addresses Team Leader 1 as 팀장님 while reporting what he heard. |
| 진태경 | 기사님 | customer_to_moving_driver | Driver | polite | Taekyung addresses the private moving-truck driver by his occupational title on the phone. |
| 이삿짐 아저씨 | 진태경 | moving_driver_to_customer | Mr. Jin Taekyung; Boss | friendly-polite | The driver uses 진태경 씨 on the phone and 사장님 while insisting on moving the capsule. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 월화 | 진태경 | Lower District Sect branch leader to Jin Family young master | Young Master Jin; our Young Master | polite and lightly playful | Uses 우리 공자님, 진 공자, and the teasing 잠룡 공자 while greeting and teasing Taekyung. |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 월화 | 진무경 | Lower District Sect Branch Leader and inn proprietress to Jin Family Second Young Master | Young Hero Jin | polite and lightly playful | At departure, Wolhwa addresses Mukyung as 진 소협 after agreeing to accompany the group. |
| 오색귀 | 진태경 | former_bandit_associates_to_prior_benefactor | Boss | pleading and deferential | The Five-Colored Ghosts repeatedly call Taekyung 대형 while begging him to rescue them. |
| 월화 | 춘삼 | Lower District Sect branch leader to subordinate | Chunsam | commanding-familiar | Uses 춘삼아 while directing him to execute the interrogation order. |
| 마적 | 풍양 | mounted-bandit subordinate to bandit leader | Leader | deferential | Uses 단주 when reporting to Pung Yang. |
| 소월 | 철무백 | niece_to_paternal_uncle | Uncle Cheol | familiar-polite | Lee Seowol asks Cheol Mubaek to suppress his heat because she cannot breathe. |
| 철무백 | 소월 | paternal_uncle_to_niece | Seowol | affectionate-familiar | Cheol Mubaek speaks gently to Seowol and says protecting her is his duty. |
| 소월 | 철검대주 | sect_leader_to_subordinate | Iron Sword Squad Leader | formal-commanding | Lee Seowol addresses him while issuing her final instruction about her title. |
| 소월 | 수문각주 | sect_leader_to_subordinate | Master of the Gatekeeper Pavilion | formal-commanding | Lee Seowol addresses him while asserting her authority as Sect Leader. |
| 사자 | 이소월 | enemy_envoy_to_sect_leader | Sect Leader | mock-formal | The Red Wind Band envoy addresses Lee Seowol as 문주님 while delivering the coercive marriage-or-destruction ultimatum. |
| 풍양 | 철무백 | junior_to_older_martial_peer | Senior Cheol | polite and taunting | Pung Yang repeatedly addresses Cheol as 철 선배 while provoking him. |
| 진태경 | 철무백 | junior_to_respected_Peak_master | Sir | apologetic-polite | Taekyung first calls Cheol Grandpa, then corrects himself to the respectful 대협. |
| 월화 | 철무백 | ally_to_injured_master | Sir Cheol | polite and reassuring | Wolhwa addresses the critically wounded Cheol while administering temporary medicine and asking about his attacker. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 이소월 | captor_to_coerced_bride | Young Lady | polite and coercive | Pung Yang addresses Seowol as 소저 while threatening her subordinates and demanding marriage. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 진태경 | 풍양 | enemy_to_enemy | you pill-popping bastard | insulting-casual | Taekyung openly insults Pung Yang while announcing that he will use a pill too. |
| 풍양 | 진태경 | enemy_to_enemy | little brat; wet-behind-the-ears fledgling | condescending and taunting | Pung Yang dismisses Taekyung as an inexperienced child while challenging his ability to intervene. |
| 무인 | 이소월 | sect_subordinate_to_sect_leader | Sect Leader | formal-deferential | Surviving Mount Heng martial artists address Seowol by her title during the casualty search. |
| 이소월 | 진태경 | rescued_sect_leader_to_benefactor | Benefactor | deferential | Lee Seowol repeatedly addresses Taekyung as 은공 after acknowledging that he and Jin Mukyung saved the Mount Heng Sword Sect. |
| 월화 | 혼주지부장 | chief_branch_leader_to_subordinate_branch_leader | Honju Branch Leader | formal-commanding | Wolhwa addresses him by branch title while directing rumor operations. |
| 진무경 | 이소월 | junior_to_sect_leader | Sect Leader | formal-polite | Uses 문주 while greeting Lee Seowol. |
| 혁무진 | 이소월 | subordinate_to_sect_leader | Sect Leader | deferential and exuberant | Formally praises the Sect Leader while greeting her. |
| 혁무진 | 철무백 | junior_to_respected_Peak_master | Great Hero Cheol | deferential | Begins a formal greeting with 철무백 대협 before being stopped. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 철무백 | 진태경 | senior_martial_peer_to_benefactor | you | casual-teasing | Uses 자네 while teasing Taekyung about his greeting and injuries. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 하오문도 | 진위경 | informant_to_lesser_family_head | Lesser Family Head | deferential | Uses 소가주님 while correcting Wikyung's misunderstanding about Mukyung's condition. |
| 현령 | 진태경 | county_official_to_celebrated_martial_artist | Great Hero Jin | formal-polite and admiring | Uses 진 대협 while praising Taekyung's alleged exploits. |
| 진태경 | 현령 | martial_artist_to_county_official | County Magistrate | polite and lightly sarcastic | Uses 현령님 while explaining that the Lesser Family Head cannot receive visitors. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 현령 | 진위경 | county_official_to_lesser_family_head | Lesser Family Head | formal-polite and deferential | Uses 진 소가주님 when asking Taekyung to convey his regards. |
| 현령 | 진무경 | county_official_to_renowned_martial_artist | Heaven Shaking Sword | formal-polite and respectful | Uses 진천검 when asking Taekyung to convey his regards. |
| 동료 쟁자수 | 석칠 | junior_colleague_to_senior_colleague | Hyung | casual-but-respectful | Calls Seokchil 형님 while inviting him to the fire and restraining him. |
| 석칠 | 동료 쟁자수 | senior_colleague_to_junior_colleague | Brat | gruff-casual | Uses 이놈아 while bantering with his fellow porter. |
| 동료 쟁자수 | 청풍 | senior_colleague_to_newcomer | Rookie | casual | Calls Cheongpung 신참. |
| 혁무진 | 아주머니 | childhood_benefactor_to_former_child | Auntie | deferential-polite | Mujin respectfully addresses the local snack-stall vendor who secretly gave him candied hawthorn when he was a child. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 우진태 | 황 소저 | host_to_five_gates_scion | Young Lady Hwang | polite and flirtatious | Woo Jintae presents Shu brocade as a gift while implying personal feelings, then retreats behind a joke. |
| 우진태 | 혁 아우 | older_friendly_sc ion_to_younger_sc ion | Little Brother Hyuk | familiar and patronizing | Woo Jintae promises the male scion an especially impressive gift. |
| 혁 아우 | 우진태 | younger_sc ion_to_older_friendly_sc ion | hyung | familiar and deferential | The scion calls Woo Jintae hyung after they have become close enough to use fraternal terms. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 우진태 | enemy_to_enemy | you / you bastard | insulting-casual | Taekyung repeatedly addresses Woo Jintae with hostile informal forms while demanding an apology and slapping him. |
| 우진태 | 진태경 | enemy_to_enemy | you / little bastard | condescending and enraged | Woo Jintae uses hostile forms such as 네놈, 애새끼, and 어린놈 while trying to intimidate Taekyung. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 산서오문   | **Five Gates of Shanxi**         |
| 일류     | **First Rate**    |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 기녀     | **courtesan**                                    |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 표국     | **Escort Bureau**                            |
| 소국주    | **Young Bureau Head**                        |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 형장      | **Brother** / **Brother [Name]**                                |
| 공자      | **Young Master**                                                |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 우진태 | **Woo Jintae** | Heir of the Seongun Escort Bureau and host of the Five Gates scions. |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 빙당호로 | **candied hawthorn skewers** | Traditional fruit skewers coated in hardened sugar; explained in a footnote. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 134
- **Aliases:** None
- **Role:** Mysterious young man encountered at Honghwa Inn; an exceptionally young Peak master whose Level Jin Taekyung cannot determine through Qi Sense; descended from the mountains to test himself against the Ten Dragons and Phoenixes
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, and a martial artist's competitive pride
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Raised by his grandfather in the mountains from age five; calls Jin Taekyung and Hyuk Mujin Benefactors after they feed him

### Childeuk.md

# Childeuk (칠득이)

- **Safe through:** Chapter 73
- **Aliases:** None
- **Role:** Illiterate servant of the Jin Family of Taiyuan and newly appointed Level 12 martial artist directly under Jin Wikyung
- **Personality:** Physically strong, diligent, gullible, and intensely excitable; readily interprets praise as recognition of exceptional talent
- **Voice:** Deferential, overeager, and breathless when speaking to Jin Wikyung
- **Relationships:** Servant under Jin Wikyung; assigned to serve Jin Mukyung and Jin Taekyung until removed from meal delivery after a misunderstanding

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 134
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a wealthy Taiyuan textile-merchant family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion; traveling as Jin Taekyung’s attendant for the City Lord’s luncheon
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad; son of the Hyuk Family Textile Shop’s owners, with a younger sibling who removed the need for him to inherit the family business

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 132
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman who won the visible exchange with Pung Yang, was then incapacitated by five concealed throwing knives, and survived the battle to recover after Taekyung's intervention; recovered enough from his Internal Injuries to return to the Jin Family of Taiyuan, though he is not yet fully recovered
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 134
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Woo Jintae.md

# Woo Jintae (우진태)

- **Safe through:** Chapter 134
- **Aliases:** None
- **Role:** Heir of the Seongun Escort Bureau and a leading scion of the current Five Gates of Shanxi; hosts its young members at Honghwa Inn and prepares for the City Lord's luncheon.
- **Personality:** Boastful, calculating, status-conscious, and manipulative; treats lavish gifts and money as tools for creating obligations, but becomes enraged and desperate when publicly humiliated.
- **Voice:** Charming and lavish in public, with polished courtesy that turns dry and contemptuous when he judges someone beneath him.
- **Relationships:** Heir to the Seongun Escort Bureau; cultivates the current Five Gates scions through hospitality, gifts, and bribes.

## Korean source

```text
＃135화



쫙!

“도, 도와주시오!”

“너 도와줄 사람 없다.”

쫙쫙!

“사, 살려 주시오!”

“싫어, 안 돼. 돌아가.”

쫙쫙쫙!

“차, 차라리 죽여…….”

“아냐, 너 아직 괜찮아. 주둥이에서 말이 나오고 있잖아.”

쫙쫙쫙쫙!

“흐윽, 흐그으윽.”

“그래, 바로 이 반응이지.”

나는 그제야 비로소 손을 멈췄다.

그럭저럭 봐줄 만했던 귀공자의 얼굴은 찐빵처럼 부풀었고, 양 뺨에는 발그레한 홍조 대신 검푸른 멍이 새겨져 있었다.

“우리 진태. 잘못했어, 안 했어.”

“흐그윽.”

엉망이 된 몰골로 흐느끼는 녀석을 보니 문득 안쓰럽다는 생각이 들었다.

그래, 얘도 남의 집 귀한 아들인데…….

“잘못했지?”

“흐극, 흐그그극!”

“그러니까 왜 사람 말을 무시해. 사과하라고 했을 때 바로 사과했으면 얼마나 좋아. 안 그래?”

“흐으으.”

“앞으로 착하게 살자. 알겠지?”

“흐그극.”

나는 맹렬하게 고개를 끄덕이는 우진태를 가만히 바라보다가 입을 열었다.

“그런데 너…….”

“흐으?”

“아까부터 대답이 왜 그따위야? 사람 말 못 해?”

순간 녀석의 흐느낌이 뚝 멎었다.

“죄, 죄송합니다.”

“할 수 있네? 할 수 있는데 안 한 거네? 왜 운 거야? 내가 이 정도로 아프고 힘들다. 뭐 그런 거 티 내는 거야?”

“아닙니다!”

“이젠 목소리도 커지네? 성량 좋다, 너. 복식 호흡 연습해? 내 고막을 터트려서 이 위기를 모면해 보겠다, 이거야?”

“아닙니다. 정말 아닙니다. 제발 이제 그만해 주십시오, 흐흐흑…….”

“어? 또 우네? 지금 울음이 나와? 네가 뭐 잘했다고 울어. 울면 인생이 끝나? 그리고 그만해 달라니. 누가 보면 내가 가해자인 줄 알겠다?”

“죄송합니다. 안 울겠습니다.”

“와, 바로 울음 그치는 것 봐. 소름 돋는 놈이네, 이거. 내가 너였으면 죄 없는 사람 건드렸다는 죄책감에 울다 지쳐서 실신했을 텐데. 너 정말 미안하긴 해?”

“자, 잠시만. 잠시만 제 얘기를 들어 주시면…….”

“듣긴 뭘 들어. 네가 말할 자격이나 있어? 여기가 무슨 연예 대상 시상식이야? 너 말하는 동안 나는 잠자코 기다리다가 훈훈하게 웃으면서 박수 쳐 주면 돼?”

“…….”

“이제는 대답도 안 하네. 넌 밥 안 먹어도 배부르겠다. 그치? 지금처럼 남의 말 아작아작 씹어 먹으면 기분 좋…….”

말을 이어 가려던 그 순간, 우진태가 번개 같은 속도로 자신의 뒤통수를 바닥에 내리찍었다.

쿵! 털썩.

안타깝다. 최소한 한 시진은 더 갈굴 수 있었는데.

혼절한 우진태를 두고 돌아서는 나에게 수많은 시선이 우수수 날아와 꽂힌다.

“성운표국의 소국주가 저렇게 간단하게…….”

“저 젊은 놈, 도대체 정체가 뭐야?”

“손속도 손속이지만, 혓바닥이 독사가 따로 없구먼.”

놀람과 두려움이 섞인 웅성거림이 일파만파 퍼져 나갔다.

1층에 자리한 손님만 자그마치 백여 명. 내 얼굴을 알아보는 이들이 나타난 것도 사실 결코 놀라운 일은 아니었다.

“사, 산서잠룡이다!”

“뭐? 태원진가의?”

“그럼 산서잠룡이 둘이겠나! 어쩐지 아까부터 눈에 익더라니.”

산서잠룡의 명성이 아주 하늘을 떨어 울리는구나.

내가 흐뭇한 미소와 함께 사람들에게 손을 흔들어 주려던 그때였다.

“확실한가? 산서잠룡이라면 작년 이맘때쯤에 홍화루에서 한 번 본 적이 있는데, 내가 기억하는 모습과는 좀…….”

“이 사람아, 그때 우리 둘이 같이 있었던 건 기억 안 나나?”

“어, 그랬던가?”

“그래, 체격이나 분위기가 많이 달라져서 그렇지, 산서잠룡이 확실하네. 태원진가의 자제라는 놈이 가문에 기녀를 데려가겠다고 온갖 진상을 부리던 모습이 아직도 눈앞에 선해.”

“…….”

젠장. 별걸 다 기억하네.

내가 머쓱한 얼굴로 손을 내리자 자기들끼리 수군거리던 손님 중 몇 명이 손을 번쩍 치켜들었다.

“그때 나도 있었소!”

“형장도?”

“똑똑히 기억하오. 저놈, 아니 저분이 계단에서 넘어지면서 내 아래 물건을 쭉 잡아당겼…… 후우, 그때만 생각하면 지금도 아찔하구려.”

“허어어, 망측한지고. 지금은 괜찮소?”

“다행히도 멀쩡하오. 뿐만 아니라 그 후로 살짝 길어진 느낌이오.”

“…….”

그게 가능해?

나는 방금 입을 연 사람에게 얼마나 커졌는지 물어보고 싶은 마음을 간신히 억눌렀다. 산서오문인지 나발인지 하는 찌꺼기들의 처리가 아직 남아 있었기 때문이다.

그런데…….

“어라?”

내 시선에 들어온 것은 나란히 대가리를 박고 있는 네 명의 후기지수와 어쩐지 목이 빳빳하게 선 혁무진이었다.

“준비 끝났습니다.”

“네가 이러라고 시킨 거냐?”

“서당 개 삼 년이면 풍월을 읊는다 했습니다. 이제 척 하면 착 아닙니까?”

“너 이 녀석……!”

나는 형용할 수 없는 감정에 사로잡혔다.

처음에는 멍청한 놈인 줄 알았는데, 갈수록 똑똑해지는 것 같다.

나 대신 지력 스탯을 찍는 게 아닌지 의심될 정도다.

“성장했구나. 매우 칭찬한다.”

“과찬의 말씀이십니다. 그보다 이들은 어찌할까요?”

“검갑 줘 봐.”

“존명.”

대하 사극의 한 장면이 따로 없다. 나는 혁무진이 내민 검갑을 받아 들고 손바닥을 내리쳤다. 그립감 좋고, 타격감도 좋다.

“다들 기상.”

말이 떨어지기가 무섭게 후기지수 네 사람이 벌떡 일어났다.

두려움 가득한 시선을 무시하며 다시 레벨창을 쭉 훑어보니 역시나 이제 간신히 일류가 될까 말까 한 녀석들이다.

“뭘 잘못했는지는 이미 알 테고…… 너희가 산서오문의 후계자들이라고?”

“예, 옛!”

“셋째 아들, 막내딸. 뭐 그런 거 아냐?”

“아닙니다!”

“확실해?”

“예, 그렇습니다!”

기합이 제대로 들어간 목소리가 객잔 내부를 쩌렁쩌렁하게 울린다. 나는 검갑을 탁탁 두드리며 중얼거렸다.

“그래? 그럼 산서오문도 별거 아니네?”

“…….”

“…….”

하나같이 수치심으로 얼굴이 붉게 달아올랐지만 아무 말도 하지 못한다.

이제는 놈들도 내 신분을 아니까.

당장 나와의 무력 차이는 둘째치고서라도, 산서오문 정도로는 태원진가의 이름 앞에서 고개를 빳빳하게 들 수 없다.

“그동안 세월 좋았다. 그치?”

“……아닙니다.”

“아니긴 뭐가 아니야. 돈 걱정 없고, 뒷배 든든하고. 그거 믿고 지금까지 짱짱하게 잘나갔을 거 아냐. 응? 여기저기 시비도 걸고 다니고.”

“…….”

“그런데 태원진가랑 항산검문 사이에 전쟁이 일어났네? 평소에 잘해 준 건 태원진가인데, 항산검문이 이기면 돌아올 보복이 무서워서 눈치 살살 보다가 여기까지 왔고. 맞지?”

“그, 그게 저희는 잘…….”

“너희 후계자라면서? 각자 소문주, 소가주. 뭐 그런 거 아니냐? 아, 저기 저놈은 소국주였지.”

엉겁결에 내가 가리키는 방향을 바라본 네 사람이 몸을 부르르 떨었다.

모진 따귀 세례와 트래쉬 토크를 견디지 못하고 스스로 기절을 택한 우진태가 죽은 것처럼 바닥에 누워 있었다.

“아무튼, 상황이 이러면 적당히 쭈그려 있지 뭐 잘났다고 여기까지 와서 기고만장하게 굴어. 태원진가가 우스워? 내가 이마에 산서잠룡이라고 문신 새기고 다녀야 해?”

“죄, 죄송합니다.”

“죄송하면 다 끝나? 내가 너희 죽사발 낸 다음에 사과해 줘?”

“히익!”

저 공포에 찬 눈빛들을 보라. 걸어 다니는 재앙이 된 기분이다.

더 이상 말이 필요 없는 상황. 나는 검갑을 들어 올렸다.

“역사적으로도 이게 약이었다. 다들 엎드려뻗쳐.”

그리고 오들오들 떨면서 엎드린 네 명의 후기지수에게 스산한 목소리로 물었다.

“몇 대 맞아야 반성할래? 각자 말해 봐.”

“예, 예?”

“말해 보라고. 우진태 저놈은 너무 나대서 저렇게 팬 거지, 너희는 자진 납세 했으니까 정상참작 해 준다.”

무거운 침묵이 흘렀다. 빠르게 시선을 교환한 네 사람이 한입으로 외쳤다.

“하, 한 대만 맞겠습니다!”

“한 대? 그걸로 되겠어?”

“옛!”

“한 대 맞으면 다시는 이런 일 없게 할 거야?”

“천지신명께 맹세하겠습니다!”

나는 검갑을 단단히 말아 쥐었다.

“좋아. 그럼 각자 열 대씩.”

“……!”

“……!”

“방금 천지신명한테 물어봤는데, 너희는 한 대로 어림도 없대. 그러니까 열 대.”

내가 살면서 이런 상황을 겪게 될 줄이야. 학창 시절, 틈만 나면 빠따를 휘두르던 체대 입시 선생이 된 기분이다.

나는 묘한 향수에 젖은 채 빠따, 아니 검갑을 휘둘렀다.

빡! 빡! 빡! 딱!

“크헉!”

“움직이지 마. 뼈 다친다. 자, 다시.”

빡! 빡! 빡!

홍화 객잔을 가득 메운 사람들에게는 진귀한 광경일 것이다. 산서오문의 후계자라는 자들이 굼벵이처럼 바닥을 기어 다니고 있었으니까. 심지어 그중에는 여자도 둘이나 끼어 있었다.

우리를 빙 둘러싼 사람들이 수군거리는 소리가 귓가를 파고들었다.

“저거, 저래도 되는 거여?”

“그러게 말이여. 아무리 그래도 산서오문인데…… 이러다가 또 무림의 은원이니 뭐니 하면서 큰 싸움 일어나는 거 아닌가 모르겄네.”

“거, 답답하기는. 요즘 상황을 몰라도 너무 모르는 거 아니오? 항산검문이 건재했다면 모를까, 지금 태원진가를 막으려면 산서 땅에 있는 중소 문파가 죄다 뭉쳐도 될까 말까요.”

“그 정도여?”

“다 끌어모으면 머릿수야 앞설지 몰라도 수준이 다르지. 저기 산서잠룡만 봐도 알 수 있는 사실 아니오?”

“그렇긴 하네. 산서오문의 후계자니, 후기지수니 뭐니 하면서 거들먹거리더니 산서잠룡한테는 쥐뿔도 안 되는 거 보면.”

“따지고 보면 먼저 시비 건 것도 저쪽 아니오?”

“그것도 맞는 말이지.”

“그리고 기왕 말이 나왔으니 말인데, 지금 산서오문이라고 하고 다니는 것들 보면 죄다 냄새가 구려.”

“구리다니?”

“말이 정파지 알게 모르게 양민 등골이나 빨아먹는다, 이 말이오. 당장 성운표국만 봐도 상인들 사이에서 얼마나 말이 많은데?”

“그 소문들이 사실이었나?”

“반면에 태원진가는 어떻소? 십 년 전에 기근(飢饉)이 들었을 때는 구휼미도 풀고, 그보다 훨씬 전에는 마교 놈들도 막아 냈지. 그놈들은 우리 같은 양민들도 죽이고 다니는 흉악한 살귀(殺鬼)들이니 만약 태원진가가 아니었다면…… 으, 생각하기도 싫소.”

“맞다, 이번에 고원에서 넘어온 마적들을 쫓아 보낸 것도 태원진가라고 들었는데.”

“그 소문 아직 못 들은 사람도 있소? 진천검과 산서잠룡이 싹 다 몰살을 시켜 버렸다고 합디다.”

“허어어.”

“그러니 만에 하나 다시 전쟁이 일어난들 문제 될 것이 무에 있겠소? 내 맹세컨대, 산서오문이 이 문제를 걸고넘어지면 당장 태원진가에 입문(入門)하여 싸우겠소!”

“오오!”

“아직 젊은 친구가 협기(俠氣)가 대단하군. 내 듣고 보니 자네 말이 맞는 것 같네. 여기 내 술 한 잔 받게!”

빡! 빡! 빡!

후기지수 넷 중 세 명을 굼벵이로 만든 나는 말소리가 들려오는 쪽으로 고개를 돌렸다.

얼마나 힘써서 태원진가를 변호해 주는지, 이야기를 듣다 보니 내가 술을 사 주고 싶어질 정도다.

‘마인드만 보면 이미 우리 태원진가 사람인데?’

레벨만 좀 받쳐 준다면 영입 1순위다. 나는 흐뭇하게 웃으며 저 위대한 웅변가의 레벨창을 확인했다.



[Lv.15 장칠득]



“……뭐여, 시벌.”

장칠득? 내가 아는 그 장칠득?

다시 잘 보니 분명 아는 얼굴이다. 진무경에게 일대일 집중 수련을 받던 시절, 우리한테 꼬박꼬박 식사를 가져다주던 하인.

바로 그 장칠득이 위대한 웅변가의 정체였다.

‘와 씨, 소름.’

어쩐지 너무 태원진가 편만 들더라.

물론 틀린 말은 없었지만 이런 식으로 여론 조작을 하다니.

뭔가 정치계의 엄청난 음모를 발견한 것 같은 기분에 몸이 부르르 떨리던 그때였다.

“저기…….”

잠시 잊고 있던 한 사람, 청풍이 맑은 눈으로 입을 열었다.

“아직 한 분 남았는데요.”

“헉.”

엎드려 있던 마지막 한 놈이 움찔했다. 청풍 이놈도 은근히 순진한 것 같으면서 무서운 놈이다.

어차피 마지막이라고 봐줄 생각 따위는 없었지만.

“안 그래도 지금 때리려고요.”

검갑을 휘두르려던 그때, 청풍이 재차 입을 열었다.

“저기. 어려운 부탁 하나만 말씀드려도 되겠습니까?”

“빙당호로 이제 없어요.”

“그게 아니고, 저어.”

머뭇거리던 청풍이 조용히 검갑을 가리켰다.

“마지막 분은 제가 한번 때려 보고 싶어서요.”

“예?”

“제가 아직 이런 걸 한 번도 안 해 봐서…….”

“…….”

살면서 별의별 또라이를 다 봤지만, 첫 경험 빌런은 처음이다.
```

## Final English reading copy

```markdown
# Chapter 135

*Smack!*

“P-please, help me!”

“No one’s coming to help you.”

*Smack-smack!*

“P-please, spare me!”

“No. Not happening. Go back.”

*Smack-smack-smack!*

“Th-then just kill me…”

“No, you’re still fine. Words are still coming out of your mouth.”

*Smack-smack-smack-smack!*

“Hhk… Hhrrgh…”

“Yes. That’s the reaction I was looking for.”

Only then did I finally stop my hand.

The young master’s face, which had been reasonably presentable until now, had puffed up like a steamed bun. Instead of a healthy flush, both cheeks were covered in dark blue bruises.

“Our Jintae. Did you do something wrong or not?”

“Hhrrgh.”

Seeing him sob with his face in such a mess, I suddenly felt a little sorry for him.

*Right. He’s someone else’s precious son, too…*

“You did something wrong, didn’t you?”

“Hhk! Hhrrgh!”

“Then why did you ignore what I was saying? You should’ve apologized the moment I told you to. Wouldn’t that have been better? Don’t you think?”

“Hhrrr.”

“Let’s live properly from now on. Understand?”

“Hhrrgh.”

I quietly watched Woo Jintae nod furiously before opening my mouth.

“But you…”

“Hh?”

“Why have you been answering like that this whole time? Can’t you speak like a normal person?”

His sobbing stopped dead.

“I-I’m sorry.”

“You could do it? You could speak, but you chose not to? Why were you crying? Were you trying to show everyone how much pain and hardship you were in?”

“No!”

“Your voice is getting louder, too. You’ve got some volume. Have you been practicing diaphragmatic breathing? Were you planning to blow out my eardrums and escape this crisis?”

“No. Absolutely not. Please, stop now. Hh-hhng…”

“Oh? You’re crying again? You can still cry? What have you done to deserve tears? Is your life over because you’re crying? And ‘please stop’? Anyone watching would think I was the one attacking you.”

“I’m sorry. I won’t cry.”

“Wow, look at him stop crying right away. You’re a creepy one, aren’t you? If I were you, I’d feel so guilty for picking on an innocent person that I’d cry until I passed out from exhaustion. Are you really sorry?”

“P-please, just listen to me for a moment…”

“Listen to what? Do you even have the right to speak? Is this some kind of entertainment awards ceremony? Am I supposed to sit quietly while you talk, then smile warmly and applaud when you’re finished?”

“…”

“Now you’re not even answering. You must feel full even without eating. Right? If you keep crunching through other people’s words like that, it must feel good…”

Just as I was about to continue, Woo Jintae slammed the back of his head into the floor with lightning speed.

*Thud! Plop.*

What a shame. I could have kept chewing him out for at least another shichen.[^1]

[^1]: A shichen is a traditional time unit equal to approximately two hours.

As I turned away from the unconscious Woo Jintae, countless gazes came flying toward me and stuck fast.

“The Young Bureau Head of the Seongun Escort Bureau went down that easily…”

“Who the hell is that young man?”

“His hands are vicious enough, but his tongue is a venomous snake all on its own.”

A murmur mixed with shock and fear spread through the room like a wave.

There were more than a hundred guests on the first floor alone. It was hardly surprising that some of them recognized my face.

“It’s the Sleeping Dragon of Shanxi!”

“What? The one from the Jin Family of Taiyuan?”

“Do you think there are two Sleeping Dragons of Shanxi? I knew his face looked familiar.”

*My reputation as the Sleeping Dragon of Shanxi really does reach the heavens.*

I was just about to give the crowd a pleased smile and wave when someone spoke up.

“Are you sure? I saw the Sleeping Dragon of Shanxi at Honghwaru around this time last year, but he looks a little…”

“You don’t remember that the two of us were there together?”

“Oh. Were we?”

“Yes. His build and overall impression have changed quite a bit, but it’s definitely him. I can still see him causing a scene because he wanted to bring a courtesan back to the Jin Family.”

“…”

*Damn. Why do people remember such useless things?*

As I awkwardly lowered my hand, several of the guests who had been whispering among themselves suddenly raised their hands.

“I was there, too!”

“You were, Brother?”

“I remember it clearly. That guy—no, that gentleman—fell down the stairs, grabbed the thing between my legs, and gave it a long yank… Whew. Just thinking about it still makes me dizzy.”

“My goodness, how indecent. Are you all right now?”

“Fortunately, I’m perfectly fine. Not only that, I think it’s gotten a little longer since then.”

“…”

*Can that happen?*

I barely managed to suppress my urge to ask the man who had just spoken exactly how much longer it had gotten. There was still the trash from the so-called Five Gates of Shanxi to deal with.

But then…

“Huh?”

What came into view were four young prodigies with their heads planted on the floor in a row—and Hyuk Mujin standing there with his head held oddly high.

“We’re ready.”

“Did you order them to do this?”

“They say that even a village-school dog can recite poetry after three years. Now, if you give me a hint, I know exactly what to do.”

“You little…”

I was seized by an indescribable emotion.

At first, I had thought he was an idiot, but he seemed to be getting smarter by the day.

I was almost suspicious that he was putting points into Intelligence for me.

“You’ve grown. I’m very proud of you.”

“You’re too kind. More importantly, what should we do with them?”

“Give me the sword case.”

“At your command.”

It was straight out of a historical drama. I took the sword case Hyuk Mujin held out and brought it down against my palm.

The grip was good, and the impact felt good, too.

“Everyone, get up.”

The four young prodigies sprang to their feet the moment I spoke.

Ignoring their terrified gazes, I scanned their Level Windows again. Just as I thought, they were barely First Rate, if that.

“You already know what you did wrong… You’re the heirs of the Five Gates of Shanxi?”

“Y-yes, sir!”

“The third son, the youngest daughter, that sort of thing?”

“No!”

“Are you sure?”

“Yes, we are!”

Their voices, filled with proper martial spirit, rang through the inn. I tapped the sword case against my palm and muttered,

“Really? Then the Five Gates of Shanxi aren’t anything special, are they?”

“…”

“…”

Every one of their faces flushed with shame, but none of them dared to answer.

They knew who I was now.

Their difference in martial power was only the second issue. Even putting that aside, people from the Five Gates of Shanxi couldn’t hold their heads high in front of the Jin Family of Taiyuan.

“You’ve had it good all this time, haven’t you?”

“…No.”

“What do you mean, no? You never had to worry about money, and you had powerful backing. You relied on that and lived large all this time, didn’t you? Picking fights wherever you went.”

“…”

“But then a war broke out between the Jin Family of Taiyuan and the Mount Heng Sword Sect. The Jin Family was the one that had always treated you well, but you were afraid of the retaliation that would come if Mount Heng won, so you kept watching the situation and ended up here. Right?”

“Th-that’s… We…”

“You’re the heirs, aren’t you? A Young Sect Leader, a Lesser Family Head—something like that, right? Ah, that fellow over there was the Young Bureau Head.”

The four people I pointed toward reflexively glanced in that direction and shuddered.

Unable to endure the merciless barrage of slaps and trash talk, Woo Jintae had chosen to pass out. He lay on the floor as though he were dead.

“Anyway, given the situation, you should’ve kept your heads down. What did you come all the way here for, acting so high and mighty? Do you think the Jin Family of Taiyuan is a joke? Do I need to tattoo ‘Sleeping Dragon of Shanxi’ on my forehead and walk around with it?”

“I-I’m sorry.”

“Does apologizing make everything go away? Should I beat you into a bloody mess and then apologize to you?”

“Eek!”

Just look at those terrified eyes. I felt like a walking disaster.

This was a situation that no longer required words. I raised the sword case.

“Historically, this has always been an effective remedy. Everyone, get down.”

Then I asked the four trembling young prodigies who lay face down in a chilling voice,

“How many blows will it take for you to reflect? Each of you, give me a number.”

“W-what?”

“Give me a number. I beat that Woo Jintae so badly because he was acting too high and mighty. Since you paid up voluntarily, I’ll take that into consideration.”

A heavy silence descended.

The four of them exchanged hurried glances before shouting as one.

“J-just one!”

“One? Will that really be enough?”

“Yes, sir!”

“If you take one hit, will you swear never to do anything like this again?”

“We swear it before Heaven and Earth and all the divine spirits!”

I gripped the sword case tightly.

“Good. Then ten each.”

“……!”

“……!”

“I just asked Heaven and Earth, and they said one wouldn’t come close to being enough for you. So ten it is.”

I never thought I’d find myself in a situation like this.

Back in school, I felt like one of those physical-education entrance-exam teachers who swung a bat whenever he got the chance.

Wallowing in a strange sense of nostalgia, I swung the bat—or rather, the sword case.

*Whack! Whack! Whack! Crack!*

“Guh!”

“Don’t move. You’ll hurt your bones. All right, again.”

*Whack! Whack! Whack!*

It must have been a rare sight for everyone filling Honghwa Inn. The heirs of the Five Gates of Shanxi were crawling across the floor like grubs.

There were even two women among them.

The whispers of the people surrounding us cut into my ears.

“Is that really okay?”

“I know, right? Even if they are the Five Gates of Shanxi… Couldn’t this turn into one of those big fights over Murim gratitude and grudges?”

“Don’t be so clueless. Are you really that out of touch with what’s happening these days? Maybe things would be different if the Mount Heng Sword Sect were still standing, but to stop the Jin Family of Taiyuan now, every small and medium-sized sect in Shanxi would have to join forces—and even then, they might not manage it.”

“It’s that bad?”

“They might have the numbers if they gathered everyone, but the caliber is completely different. You only have to look at the Sleeping Dragon of Shanxi over there to know that.”

“That’s true. Those Five Gates heirs swaggered around acting so important, but they’re completely worthless in front of the Sleeping Dragon of Shanxi.”

“If you think about it, they were the ones who picked the fight first.”

“That’s true, too.”

“And since we’re on the subject, there’s something rotten about all those people who call themselves the Five Gates of Shanxi these days.”

“Rotten?”

“They call themselves an orthodox faction, but they’re really just sucking the marrow out of ordinary people without anyone noticing. Just look at the Seongun Escort Bureau. How many complaints have merchants made about them?”

“Were all those rumors true?”

“What about the Jin Family of Taiyuan? When there was a famine ten years ago, they released relief grain. Long before that, they even held off the Demonic Cult. Those bastards were vicious murderers who went around killing ordinary people like us. If not for the Jin Family of Taiyuan…”

“Ugh. I don’t even want to think about it.”

“That’s right. I also heard it was the Jin Family of Taiyuan that drove off the mounted bandits who came over from Gaoyuan this time.”

“Is there anyone who hasn’t heard that rumor yet? They say the Heaven Shaking Sword and the Sleeping Dragon of Shanxi slaughtered every last one of them.”

“My goodness.”

“So even if another war breaks out, what’s there to worry about? I swear, if the Five Gates of Shanxi try to make an issue of this, I’ll join the Jin Family of Taiyuan and fight alongside them!”

“Oh!”

“That’s some impressive chivalrous spirit for such a young man. Now that I’ve heard you out, I think you’re right. Here, have a drink on me!”

*Whack! Whack! Whack!*

I had turned three of the four young prodigies into grubs when I turned my head toward the voices.

They were defending the Jin Family of Taiyuan with such passion that, by the time I finished listening, I almost wanted to buy them a drink.

*In terms of mindset, he’s already one of our Jin Family.*

If his Level were high enough, he’d be my first pick for recruitment. Smiling with satisfaction, I checked the Level Window of the great orator.

> **System**
>
> **Level 15: Jang Childeuk**

“…What the fuck?”

*Jang Childeuk? The Jang Childeuk I know?*

Looking again, I realized that I definitely knew the face.

He was the servant who had brought us meals every day while I was receiving one-on-one intensive training from Jin Mukyung.

That Jang Childeuk was the great orator’s true identity.

*Holy shit. Goose bumps.*

No wonder he had been taking the Jin Family’s side so aggressively.

He hadn’t said anything incorrect, of course, but manipulating public opinion like this…

Just as I trembled at the feeling that I had uncovered some enormous conspiracy in the political world, someone spoke up.

“Um…”

It was Cheongpung, the one person I had momentarily forgotten. He opened his mouth with his clear eyes shining.

“There’s still one person left.”

“Ah.”

The last man lying face down flinched. Cheongpung seemed innocent in his own way, but he was also strangely frightening.

Not that I had any intention of going easy on him just because he was last.

“I was just about to hit him.”

I was about to swing the sword case when Cheongpung spoke again.

“Excuse me. May I ask you one difficult favor?”

“We’re out of candied hawthorn skewers[^2] now.”

[^2]: Candied hawthorn skewers are a traditional snack of fruit skewers coated in hardened sugar.

“That’s not it. I, uh…”

Cheongpung hesitated, then quietly pointed at the sword case.

“I’d like to try hitting the last gentleman once.”

“What?”

“I’ve never done anything like this before…”

“…”

I had seen every kind of nutcase in my life, but this was my first time seeing a first-experience villain.
```
