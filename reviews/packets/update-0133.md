<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0133.txt",
      "sha256": "4294dc1b4df15deaad1baf2871359712e69817fb47f8c8edb94a7e5a0bdf2aef",
      "bytes": 13768
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b0c6c43dcb41d9185995dac700728f0bcb3a5721d9ae289df68ee8516e5e1853",
      "bytes": 7685
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a11145102551e7093efdd0d73a22707136c23397b86b523b2a99e3e093753a99",
      "bytes": 24992
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "430b2e4c0614a6d37f867e37a58781197aac5340bdfc872ab745a56c1b683075",
      "bytes": 719
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "b508d5a010e8d6bd03d323da739583e98ff172962e1a0df0adf4b814e42878de",
      "bytes": 5353
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2e93dbdb638822fa51c83a69d1adc3f6427598ab17c2d040556e146b76fc4fa1",
      "bytes": 21214
    }
  ],
  "estimated_tokens": 22351
}
-->

# Durable State Update — Chapter 133

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 133. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 133. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 133,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 133,
    "continuity_sources": [133],
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
    "Seokchil is a middle-aged porter with nearly twenty years of experience at the Seongun Escort Bureau in southern Shanxi Province.",
    "Cheongpung is an eccentric former porter who recently fled Huashan's Lotus Peak and traveled toward Taiyuan; he is an exceptionally young Peak master whose Level Taekyung cannot determine through Qi Sense, lived with his grandfather in the mountains from age five, and came down to test himself against the Ten Dragons and Phoenixes.",
    "Hyuk Mujin's parents are healthy textile merchants in Taiyuan who own the city's largest textile shop, with branches in Henan and Hebei; Mujin left home to avoid inheriting the business, and a younger sibling later removed that obligation.",
    "Taekyung has begun treating Hyuk Mujin as a valued companion rather than merely a subordinate, acknowledging the hardship Mujin endured while traveling with him.",
    "Five silk-clad men and women on Honghwa Inn's second floor mocked Taekyung, Mujin, and Cheongpung; their identities are unknown."
  ],
  "continuity_sources": [
    132,
    131
  ],
  "open_questions": [
    "How will the Jin Family of Taiyuan respond to Lee Seowol's proposed transaction and territorial transfer?",
    "Can Lee Seowol preserve or rebuild the Mount Heng Sword Sect with so few survivors?",
    "What are the Temporary Strength Pill's exact price and long-term aftereffect, and is it related to the Demonic Cult's Blood-Exploding Pill?",
    "What is Dark Heaven, and why do Jin Wikyung and Wipeng refuse to discuss it?",
    "What consequences will Pung Yang's death have for the Red Wind Band and the wider Murim?",
    "Is the Fire King still alive, and if so, where is he?",
    "What will happen at the City Lord's luncheon and how will the City Lord react to Taekyung?",
    "What was Cheongpung's status at Huashan's Lotus Peak, who is his grandfather, and who are the five silk-clad people mocking the group?"
  ],
  "safe_through": 132,
  "temporary_decisions": [
    "Render 잠력단 as Temporary Strength Pill and 폭혈단 as Blood-Exploding Pill.",
    "Render 만년한철 as Ten-Thousand-Year Cold Iron and 이름 없는 검 as Unnamed Sword.",
    "Render 열화신단 as Blazing Flame Divine Pill and 반 갑자 as half a jiazi, clarified as thirty years of internal energy.",
    "Render 완전 회복 as Full Recovery and 회광반조 as final rally in this death-and-recovery context.",
    "Render 운칠기삼 as seven parts luck and three parts skill, and 운구기일 as nine parts luck and one part qi, with a footnote explaining the variation.",
    "Render 은공 as Benefactor, 절정 무공 as Peak martial arts, 급식 as school lunch, 고딩 as high schooler, 철컹 as clank, 산서성 as Shanxi Province, 총지부장 as Chief Branch Leader, 원단 as New Year's Day, 갑자 as jiazi, 시진 as shichen, 표행 as escort run, 쟁자수 as porter, 표국 as Escort Bureau, 표두 as Escort Chief, 은원보 as silver ingot, 은자 as nyang of silver, 사서삼경 as the Four Books and Three Classics, and 연화봉 as Lotus Peak.",
    "Render 일인전승 as single successor, 비인부전 as transmission only to the worthy, 구 대 계승자 as ninth-generation successor, 천하십대권법 as the ten greatest fist techniques in the world, 열화문 as Fire Gate Clan, 화왕 as Fire King, 삼성 as Three Saints, 십왕 as Ten Kings, 진무보법 as Jin Family's Manoeuvre Technique, 아이템창 as Item Window, 전서응 as messenger eagle, 고원 as Gaoyuan, 구주 as Nine Provinces, 사술 as dark arts, 마기 as demonic qi, 선천지기 as innate qi, 소음인 as Soeumin, 태양인 as Taeyangin, 암천 as Dark Heaven, 주신 as God of Drinking, 야왕 as Night King, 화주 as fire liquor, 화북 as North China, 현령 as county magistrate, 성주 as City Lord, 장 노인 as Old Man Jang, 적토마 as Red Hare, 여포 as Lü Bu, 성주의 초청 as The City Lord's Invitation, 친왕 as Prince, 주씨 as Zhu, 천자 as Son of Heaven, 황상 and 황제 as Emperor, 태자 as Crown Prince, 구파일방 as Nine Sects and One Gang, and 오대세가 as Five Great Families; render 개방 as Beggars' Sect and 십봉룡 as Ten Dragons and Phoenixes.",
    "Render 빙당호로 as candied hawthorn skewers with an explanatory footnote; render 산니백육 as Garlic Pork, 어향육사 as Fish-Fragrant Shredded Pork, 경장육사 as Beijing Sauce Shredded Pork, 규화계 as Beggar's Chicken, 매구 as Maegu, and 매채구육 as Maechae Guyuk with a footnote explaining the abbreviation; render 혁가 포목점 as Hyuk Family Textile Shop and 하북 as Hebei."
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

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 산서오문   | **Five Gates of Shanxi**         |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 삼류     | **Third Rate**    |
| 일류     | **First Rate**    |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 기루     | **pleasure house**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 표국     | **Escort Bureau**                            |
| 레벨               | **Level**                      |
| 매력               | **Charm**                      |
| 산서     | **Shanxi**             |
| 사천     | **Sichuan**            |
| 팔천협    | **Eight Spring Gorge** |
| 귀문      | **your sect**                                                   |
| 귀가      | **your family**                                                 |
| 소협      | **Young Hero**                                                  |
| 소저      | **Young Lady**                                                  |
| 대사      | **Master** for a senior Buddhist monk                           |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 삼문협 | **Three Questions Gorge** | A distant gorge and route connecting Shanxi with Shaanxi and Henan. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 132
- **Aliases:** None
- **Role:** Mysterious young man encountered at Honghwa Inn; an exceptionally young Peak master whose Level Jin Taekyung cannot determine through Qi Sense; descended from the mountains to test himself against the Ten Dragons and Phoenixes
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity and a martial artist's competitive pride
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Raised by his grandfather in the mountains from age five; calls Jin Taekyung and Hyuk Mujin Benefactors after they feed him

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 132
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a wealthy Taiyuan textile-merchant family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion; traveling as Jin Taekyung’s attendant for the City Lord’s luncheon
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad; son of the Hyuk Family Textile Shop’s owners, with a younger sibling who removed the need for him to inherit the family business

## Korean source

```text
＃133화



우진태(優進泰)는 황금빛 술잔을 치켜들었다. 온갖 진미와 명주로 가득 채워진 탁자에는 그를 포함하여 총 다섯 명의 남녀가 앉아 있었다.

“자, 산서오문(山西五門)의 무궁한 발전을 위하여!”

“위하여!”

“위하여!”

한 순배씩 술이 돌자 다섯 사람의 얼굴에 웃음이 번졌다.

“역시 홍화객잔이군요. 숙수가 누군지는 몰라도 음식 맛이 대단합니다.”

“그러게요. 혀에 닿자마자 살살 녹아요.”

우진태가 호탕한 웃음을 터트렸다.

“하하, 허리띠 풀고 마음껏 드시오. 오늘도 내가 모두 살 테니.”

“이야, 역시 형님! 이러다가 성운표국 기둥뿌리 하나 뽑는 거 아닙니까?”

“어머, 감당되시겠어요?”

우진태는 피식 웃으며 눈앞의 이남이녀(二男二女)를 바라보았다.

스무 개의 중소 문파 연합. 그중에서도 대표 격인 산서오문의 자제들이지만 자신에게는 한 수 접어 줘야 한다.

“어허, 나 우진태요. 성운표국의 우진태! 이 객잔을 통째로 사도 문제없으니 걱정 말고 마음껏 드시오.”

약간의 허세가 섞이긴 했지만 아주 틀린 말도 아니다.

삼문협(三門峽) 일대를 주름잡고 있는 성운표국은 운수와 경비 등, 각종 사업으로 매해 엄청난 재물을 벌어들이고 있으니까.

우진태는 바로 그 성운표국을 물려받을 후계자였다.

‘역시 돈이 최고지.’

산서오문이라고 해 봤자 어차피 하나같이 고만고만한 중소 문파의 자제들. 성운표국의 금력(金力)을 등에 업은 그는 거칠 것이 없었다.

“이 자리에 있는 분들 덕분에 우리 성운표국이 한 계단 올라섰으니 그만한 대접을 해야 하지 않겠소?”

우진태의 말에 사람들이 황급히 손사래를 쳤다.

“어휴, 그게 어떻게 저희 덕분입니까? 다 국주님과 형님께서 표국의 발전을 위해 불철주야 애쓰신 덕분이지요.”

“맞아요. 우 소협의 말씀은 저희가 감당하기 어려워요.”

금이면 귀신도 부린다는데 산 사람은 오죽할까.

‘불철주야 애썼다라. 뭐, 틀린 말은 아니군.’

뼈대 있는 무가(武家)도, 그렇다고 뚜렷한 무림 문파도 아닌 성운표국이 산서오문에 들어갈 수 있었던 이유는 재물을 풀었기 때문이다.

이십여 개 중소 문파의 문주들과 중진들, 자제들…… 그들 모두에게 밤낮 가리지 않고 술과 재물을 퍼먹였고, 결과는 확실했다.

‘산서오문.’

남부에 위치한 중소 문파 연합의 대표라 할 수 있는 자리다.

평범한 무림 문파였다면 허울만 좋은 명예직이었겠지만. 각종 사업을 통해서 이익을 창출하는 성운표국으로서는 날개를 단 것이나 다름없었다.

우진태는 짐짓 진중한 얼굴로 고개를 숙였다.

“아닙니다. 여러분들이 있기에 지금의 성운표국이 있는 거요. 몇 달 전만 하더라도 그 간악한 노괴(老怪)들 때문에 통 기를 못 펴고 살았는데…… 다시 한번 고맙소.”

“노괴들이라면, 그 배반자들 말입니까?”

“어이쿠, 그자들 이야기는 꺼내지도 마십시오. 이번 일이 아니었다면 우리 모두 꼼짝없이 이용만 당할 뻔했습니다.”

이 자리에 모인 이들은 모두 산서오문의 자제들이지만 불과 몇 달 전까지만 해도 아니었다.

삼도문, 궁귀문을 비롯한 다섯 개 문파, 그들이 바로 전(前) 산서오문이다. 그러나 대장로의 수족임이 밝혀진 팔천협 전투에서 빠짐없이 멸문당했다.

“이제 와서 하는 말인데, 그 작자들이 유난히 성운표국을 견제하긴 했습니다.”

“국주님과 우 소협의 혜안(慧眼)에 정체가 발각될까 봐 그런 것이 분명해요.”

우진태는 터져 나오려는 웃음을 억눌렀다. 전 산서오문의 문주들이 성운표국을 견제했던 이유는 간단하다.

‘바로 지금 같은 상황을 우려해서지.’

당시의 산서오문은 지금보다 훨씬 강했고 유대도 끈끈했다.

하지만 이제는 아니다. 이 자리의 모두는 이미 성운표국의 돈맛을 봤다. 이걸 빌미로 야금야금 각종 이권을 뺏어 먹는 건 시간문제다.

“자, 이번에는 우리의 우정을 위해 건배합시다.”

“우정을 위하여!”

흥겨운 분위기의 술자리가 이어졌다. 우진태는 틈틈이 선물이라는 이름의 뇌물을 건네기도 했다.

“이번에 사천에서 들여온 촉금(蜀錦)인데, 황 소저께 잘 어울릴 것 같아 따로 빼 두었지요.”

“어머, 제가 아는 그 촉금이요?”

“예. 그중에서도 최상급이라 그런지 빛깔이 아주 곱더군요. 하인에게 일러 마차에 미리 실어 두었으니 가져가십시오.”

“세상에, 우 소협. 너무 감사해요.”

“감사할 것까지 있겠습니까? 그냥 소저를 생각하는 제 마음이다, 생각하시고 넣어 두십시오.”

“네, 네?”

“하하, 제가 말실수를 했군요. 못 들은 셈 치십시오.”

우진태의 매력적인 미소에 소속된 무인만 일백이 넘어가는 문파의 무남독녀가 볼을 붉혔다.

마음의 빚을 지게 해 두면 언제고 써먹을 날이 있을 것이다.

“형님, 이거 서운합니다. 소저들만 챙기시는 게 어디 있습니까?”

그는 어느새 호형호제하게 된 무가의 자제를 향해 이번엔 눈을 찡긋했다.

“내가 혁 아우를 잊었을 리가. 기대하고 있게. 아주 끝내주는 선물을 준비해 뒀으니.”

“크, 역시 형님.”

“하하, 우 소협, 날 잊은 건 아니겠지요?”

“무슨 그런 섭섭한 말씀을 하십니까. 사람마다 어울리는 선물이 있어서 따로 말씀드리려고 한 것뿐입니다.”

쉬운 일이다. 여인들에게는 값비싼 비단과 보석, 사내들에게는 절색의 여인과 재물을 안겨 주면 된다.

마침 근처에 산서성 제일의 기루라는 홍화루가 있으니 안성맞춤이다.

우진태는 기뻐하는 사람들을 보며 빙긋 웃었다.

“기분도 적당히 풀렸겠다, 오늘 술자리는 이쯤에서 파할까 하는데…… 다들 어찌 생각하십니까?”

선물을 받기 전이라면 아쉬웠겠지만 지금은 다르다.

여인들은 마차에 실어 둔 비단과 보석을 확인하고 싶어 고개를 끄덕였고, 사내들은 기루로 자리를 옮길 거라는 확신에 가슴이 뛰었다.

“그럼 마지막으로 몇 잔씩들 하고 일어납시다. 내일 있을 오찬(午餐)도 잊지 마시고요.”

우진태의 말에 사람들이 피식피식 웃었다.

“아무리 취해도 그걸 잊겠습니까.”

“우 소협도 참, 저희를 너무 무시하는 것 아니에요?”

“혹시나 하는 마음에 말한 겁니다. 하하하.”

산서 성주와의 오찬.

그것이 산서에서 방귀 좀 뀐다는 문파의 자제들이 한자리에 모인 이유였다. 우진태는 술잔을 비우며 생각했다.

‘내일이 기대되는군.’

고작 열 살밖에 되지 않은 어린 성주.

사람 비위 맞추는 데에는 도가 튼 그다. 이미 성주를 구워삶을 만반의 준비를 끝내 두었다.

‘듣기로는 제법 잔망스러운 녀석이라던데…… 황족이라, 과연 어떨까?’

우진태가 곰곰이 생각에 잠겨 있던 그때. 아래층에서 쩌렁쩌렁한 외침이 터져 나왔다.

“정파 무림 최고의 후기지수들! 차기 무림을 이끌어 갈 용과 봉황들! 십봉룡을 모른다는 게 말이나 됩니까?”

“야, 야. 목소리나 줄여. 사람들 쳐다보잖아.”

십봉룡? 그 단어에 다섯 쌍의 귀가 쫑긋 섰다.

십봉룡이 누구인가, 이미 전설의 첫 장을 쓰고 있는 천재들이자 정파 무림의 미래다.

십봉룡은 강호의 후기지수들에게는 선망의 대상이었고, 이 자리에 모인 이들에게도 크게 다르지 않았다.

“누구지? 무림인인가?”

난간 가장 가까이에 앉아 있던 사람이 목을 빼고 아래층을 내려다보며 말했다.

“세 명입니다. 한 명은 도련님, 한 명은 그럭저럭 무인 같고…… 다른 하나는 거지로 보이는데요.”

“그게 도대체 무슨 조합이야?”

“쉿, 계속 들어나 봅시다.”

우진태의 말에 사람들이 입을 다물고 다시 귀를 기울였다.

다들 무가의 자제라고 할 만큼 무공을 익힌 몸이라 대화를 듣는 것은 그리 어렵지 않았다.

“말씀 계속하시죠.”

“별건 아니에요. 순간적으로 치기 어린 생각이 들었던 거죠.”

잠깐의 침묵. 그리고 이어지는 한마디.

“나와 저들 중에 누가 더 강할까? 저는 그 의문에 대한 답을 확인하고 싶었어요.”

산서오문의 후기지수들이 서로를 바라보았다.

“방금 저 말, 다들 들으셨습니까?”

“네, 누가 한 말이에요?”

“아까 말했던 그 거집니다. 요즘 별 미친놈을 다 보겠네요.”

그때 우진태가 고개를 저었다.

“거지가 아니라 무인일 겁니다.”

“무인……이라고 하셨습니까?”

“십봉룡을 입에 올릴 정도면 그게 맞겠죠. 어떻게 거지꼴이 됐는지는 뭐, 안 봐도 대충 알겠고요.”

우진태의 입가에서 실소가 흘러나왔다.

“뻔하지 않습니까. 어쩌다 익힌 삼류 무공 몇 수를 믿고 하염없이 강호를 떠돌다가 죽는 인생.”

“아하, 생각해 보니 그렇네요. 역시 우 소협이십니다.”

“곱씹을수록 웃기네. 어떻게 저 주제에 십봉룡을 입에 올렸지?”

서로를 바라보며 피식거리던 후기지수들의 웃음이 점점 진해졌다.

“그런 정신 나간 놈이랑 어울리는 것들 수준도 알 만하군. 아니, 미친놈이라고 따귀를 한 대 올려붙이고 나가려나?”

“그, 같이 앉은 도련님이랑 무인은 뭐 하고 있대요?”

아래를 힐끗 내려다본 후기지수가 웃음을 참으며 말했다.

“무인은 모르겠고, 도련님은 혼자서 고개 끄덕끄덕하고 있습니다.”

“허어.”

“정말요?”

“이야, 다들 저 표정을 봐야 되는데. 진심으로 저 거지 말을 믿는 것 같은데요?”

후기지수들이 자리에서 일어나 난간으로 다가갔다. 그중에는 호기심을 참지 못한 우진태도 포함되어 있었다.

‘어떤 놈들인지 얼굴이나 보자.’

그리고 심각한 표정으로 고개를 끄덕이는 도련님의 얼굴을 본 순간, 그의 입에서 커다란 웃음이 터져 나왔다.

“푸하하핫!”

동시에 다른 후기지수들도 큰 소리로 웃기 시작했다.

“큭, 크크큭! 아, 웃음 참느라 혼났네.”

“크하하! 무공이라고는 쥐뿔도 모르는 놈들이, 뭐? 십봉룡이 어쩌고 저째?”

얼마나 웃었을까. 간신히 웃음을 그쳤을 때 그들이 목격한 것은, 물끄러미 자신들을 바라보는 한 사람의 시선이었다.

“다 웃었냐?”

‘도련님’의 한마디에 후기지수들은 멍해졌다.

다들 애지중지 자란 몸이다. 도대체 이게 얼마 만에 들어 보는 반말인가.

순간 싸하게 내려앉은 침묵을 깨트린 것은 우진태의 메마른 목소리였다.

“그렇다면?”

‘도련님’이 활짝 웃었다.

“당장 내려와, 이 호로 쌍노무 새끼들아. 목 아파.”



* * *



혁무진이 기대 어린 눈빛으로 물었다.

“한판 하시게요?”

“저놈들 하는 거 봐서.”

“호로 쌍노무 새끼 소리 나왔으면 싸우자는 거 아니에요?”

“그것도 좋고. 내 얼굴에 저놈들 침 다 튄 거 보여?”

“흥건하네요.”

혁무진이 옷소매로 내 얼굴을 슥슥 문질러 주었다.

“사과 안 하면 어떡해요?”

“해야 될걸?”

“쟤들 표정 보세요. 절대 사과 안 해요.”

“그럼 뒤지게 맞아야지.”

“여인들도 있는데…….”

“나 남녀평등주의자야.”

“예?”

“공평하게 다 때린다고.”

멍하니 구경만 하고 있던 청풍이 반짝거리는 시선으로 날 바라봤다.

“오, 잘은 모르지만 뭔가 멋있어 보여요.”

“별걸 다…… 일단 감사합니다.”

뭔가 더 얘기하고 싶어도 더 이상 시간이 주어지지 않았다.

다섯 놈, 아니 다섯 연놈들이 2층에서 훌쩍 뛰어내렸기 때문이다.

타닥.

일류 고수다운 사뿐하게 착지. 이쪽을 노려보는 그들 사이로 한 사람이 나섰다.

45레벨. 키 크고 훈훈하게 생긴 놈. 아까 처음으로 웃었던 그놈이다.

“나는…….”

“네가 대가리야?”

“대가리?”

“거기 다섯 명 중에 두목이냐고.”

놈이 피식 웃었다.

“입조심하는 게 좋을 거다. 나를 포함해서 여기 있는 분들이 누군지 알면…….”

나는 마주 웃으며 연놈들의 레벨창을 쭉 읽었다.

“성룡이, 천우, 명화, 소혜, 마지막으로 넌 진태. 성까지 말해 줘?”

“……!”

“……!”

놀라움에 찬 다섯 쌍의 눈동자. 아니, 혁무진과 청풍까지 일곱 쌍의 눈동자가 내게 쏠렸다.

“아, 그리고 이건 개인적인 부탁인데, 제발 어떻게 알았냐고 물어보지 마라. 그 대사 이제 지겨워. 말하면 때릴 거야.”

“어떻게……!”

“귀에 무 박았냐?”

다음 순간, 내 손바닥이 놈의 뺨에 닿았다.

쫙!
```

## Final English reading copy

```markdown
# Chapter 133

Woo Jintae raised a golden wine cup. Five men and women, including him, sat around a table laden with every kind of delicacy and fine liquor.

“Now, to the limitless prosperity of the Five Gates of Shanxi!”

“To prosperity!”

“To prosperity!”

After the wine made its way around once, smiles spread across everyone’s faces.

“As expected of Honghwa Inn. I don’t know who the chef is, but the food is incredible.”

“Right? It practically melts the moment it touches your tongue.”

Woo Jintae let out a hearty laugh.

“Ha-ha! Loosen your belts and eat to your hearts’ content. I’m paying for everyone today, too.”

“Wow, as expected of you, hyung! At this rate, aren’t you going to pull up one of the foundation pillars of the Seongun Escort Bureau?”

“Oh my, can you afford all this?”

Woo Jintae chuckled as he looked at the two men and two women in front of him.

They were the scions of the Five Gates of Shanxi, the representatives of an alliance of twenty small and medium-sized sects. Even so, they had to yield to him.

“Hey, I’m Woo Jintae. Woo Jintae of the Seongun Escort Bureau! I could buy this entire inn and it wouldn’t be a problem, so don’t worry and eat as much as you like.”

There was a little bit of boasting mixed in, but it wasn’t entirely untrue.

The Seongun Escort Bureau dominated the area around Three Questions Gorge and earned an enormous amount of money every year through various businesses, including transportation and security.

Woo Jintae was the heir who would inherit that very Seongun Escort Bureau.

*Money really is the best.*

The Five Gates of Shanxi were nothing more than the scions of a bunch of small and medium-sized sects that were all roughly the same. With the financial power of the Seongun Escort Bureau behind him, there was nothing Woo Jintae had to fear.

“Thanks to everyone here, our Seongun Escort Bureau has climbed another step higher, so it’s only right that I treat you accordingly, isn’t it?”

At Woo Jintae’s words, everyone hurriedly waved their hands.

“Oh, no. How could that be thanks to us? It’s all thanks to the Chief and Young Hero Woo working tirelessly day and night for the growth of the Escort Bureau.”

“That’s right. We could never accept such praise from Young Hero Woo.”

They said that money could make even ghosts do your bidding. Living people were even easier.

*Working tirelessly day and night, huh? Well, that isn’t entirely wrong.*

The Seongun Escort Bureau was neither a prestigious martial family nor a distinct Murim sect. The reason it had been able to join the Five Gates of Shanxi was because it had opened its purse.

The Sect Leaders, senior members, and scions of more than twenty small and medium-sized sects…

Woo Jintae had stuffed all of them with liquor and money day and night, and the results had been undeniable.

*The Five Gates of Shanxi.*

It was a position that could be called the representative of the alliance of small and medium-sized sects in the south.

For an ordinary Murim sect, it would have been nothing more than a hollow honorary position. But for the Seongun Escort Bureau, which generated profits through all kinds of businesses, it was like growing wings.

Woo Jintae lowered his head with an appropriately solemn expression.

“No. The Seongun Escort Bureau of today exists because of all of you. Just a few months ago, those vile old monsters had us living without being able to hold our heads up… Thank you once again.”

“Those old monsters? You mean the traitors?”

“Ugh, don’t even mention them. If this hadn’t happened, all of us would have been helplessly used by them.”

Everyone gathered here was a scion of the Five Gates of Shanxi, but that had not been the case until only a few months ago.

The Samdo Sect, the Gunggui Sect, and three other sects had been the former Five Gates of Shanxi. But during the Battle of Eight Spring Gorge, it was revealed that they were all agents of the Head Elder, and every one of them had been annihilated.

“Now that I think about it, those bastards were especially wary of the Seongun Escort Bureau.”

“They must have been afraid that their identities would be exposed by the keen insight of the Chief and Young Hero Woo.”

Woo Jintae suppressed the laugh that was threatening to escape.

The reason the former Five Gates of Shanxi had been wary of the Seongun Escort Bureau was simple.

*They were worried about exactly this situation.*

The Five Gates of Shanxi had been much stronger back then, and their bonds had been far tighter.

But that was no longer the case. Everyone here had already tasted the money of the Seongun Escort Bureau. Using that as leverage to slowly siphon away all kinds of business interests was only a matter of time.

“Now, let’s raise a toast to our friendship.”

“To friendship!”

The lively drinking continued. From time to time, Woo Jintae also handed out bribes disguised as gifts.

“This is Shu brocade I brought in from Sichuan. I thought it would suit Young Lady Hwang, so I had it set aside separately.”

“Oh my! You mean the Shu brocade I know?”

“Yes. It’s the finest grade, and perhaps that’s why the color is so exceptionally beautiful. I told a servant to load it into the carriage beforehand, so please take it with you.”

“My goodness, Young Hero Woo. Thank you so much.”

“Is there any need to thank me? Just think of it as the feelings I have for you and put it away.”

“Wh-what?”

“Ha-ha, I misspoke. Pretend you didn’t hear that.”

At Woo Jintae’s charming smile, the only daughter of a martial sect with more than a hundred affiliated martial artists blushed.

*Once I make her indebted to me, there will be a day when I can put that debt to use.*

“Hyung, this is unfair. How can you only take care of the young ladies?”

He winked at the scion of a martial family who had become close enough with him to call each other hyung and little brother.

“Did you think I could forget Little Brother Hyuk? Just wait. I’ve prepared an absolutely incredible gift for you.”

“Damn, as expected of you, hyung.”

“Ha-ha, Young Hero Woo, you haven’t forgotten me, have you?”

“What a hurtful thing to say. I only wanted to tell you separately because I have a gift suited to each person.”

It was easy. Expensive silk and jewelry for the women, and peerless beauties and wealth for the men.

There happened to be Honghwaru, supposedly the finest pleasure house in Shanxi Province, nearby. It was perfect.

Woo Jintae smiled as he watched everyone’s delight.

“Now that everyone’s had a chance to unwind, how about we end tonight’s drinking here… What do you all think?”

If they had not received their gifts yet, they might have been disappointed. But things were different now.

The women nodded because they wanted to check the silk and jewelry loaded into the carriage, while the men’s hearts pounded at the certainty that they would be moving to the pleasure house.

“Then let’s have a few final cups before we leave. And don’t forget tomorrow’s luncheon.”

Everyone chuckled at Woo Jintae’s words.

“How could we forget that, no matter how drunk we get?”

“You really underestimate us, Young Hero Woo.”

“I only mentioned it just in case. Ha-ha-ha.”

A luncheon with the City Lord of Shanxi.

That was why the scions of the sects with some clout in Shanxi had gathered in one place. Woo Jintae emptied his wine cup and thought,

*Tomorrow should be interesting.*

The City Lord was only ten years old.

He was already an expert at catering to people’s whims. Woo Jintae had finished making every possible preparation to win the City Lord over.

*I hear he’s quite a mischievous little fellow… He’s a member of the imperial family, so I wonder what he’ll be like.*

Just as Woo Jintae was sinking into thought, a booming shout erupted from downstairs.

“The greatest young prodigies of the Murim’s orthodox faction! The dragons and phoenixes who will lead the Murim of the future! How can you say you don’t know the Ten Dragons and Phoenixes?”

“Hey, hey. Keep your voice down. People are staring.”

At the words *Ten Dragons and Phoenixes*, five pairs of ears perked up.

Who were the Ten Dragons and Phoenixes? They were geniuses already writing the first pages of their legends and the future of the Murim’s orthodox faction.

The Ten Dragons and Phoenixes were objects of admiration for the young martial artists of the martial world, and the people gathered here were no different.

“Who are they? Are they martial artists?”

The person seated closest to the railing craned his neck and looked down at the first floor.

“There are three of them. One is a young master, one looks more or less like a martial artist… and the other one looks like a beggar.”

“What kind of combination is that?”

“Shh. Let’s keep listening.”

At Woo Jintae’s urging, everyone fell silent and pricked up their ears again.

They had all trained in martial arts as befitted scions of martial families, so overhearing the conversation was not difficult.

“Please continue.”

“It’s nothing important. I just had a childish thought for a moment.”

There was a brief silence. Then another statement followed.

“Who would be stronger, me or them? I wanted to find the answer to that question.”

The young prodigies of the Five Gates of Shanxi looked at one another.

“Did you all hear what he just said?”

“Yes. Who said it?”

“That beggar I mentioned earlier. You really do see all kinds of lunatics these days.”

Woo Jintae shook his head.

“He’s a martial artist.”

“A martial artist…?”

“If he’s talking about the Ten Dragons and Phoenixes, he must be. As for how he ended up looking like a beggar, I can more or less guess without even seeing it.”

A mocking laugh escaped Woo Jintae’s lips.

“Isn’t it obvious? He’s the type who picks up a few Third Rate martial arts moves by chance, puts his faith in them, wanders aimlessly through the martial world, and winds up dead.”

“Ah, now that you mention it, you’re right. As expected of Young Hero Woo.”

“The more I think about it, the funnier it gets. How did someone like that dare mention the Ten Dragons and Phoenixes?”

The young prodigies snickered at one another, and their laughter gradually grew louder.

“You can tell what kind of people associate with a lunatic like that. Or maybe they’ll slap him once, call him crazy, and leave?”

“What are the young master and the martial artist sitting with him doing?”

The young prodigy who had glanced down again spoke while trying to hold back his laughter.

“I don’t know what the martial artist is doing, but the young master is nodding to himself.”

“Huh.”

“Really?”

“Wow, you should all see his expression. He genuinely seems to believe that beggar.”

The young prodigies stood up and moved toward the railing. Woo Jintae, who could not resist his curiosity, was among them.

*Let’s see what these people look like.*

The moment he saw the young master’s face, which was nodding with a serious expression, a loud laugh burst from Woo Jintae’s mouth.

“Puhahaha!”

At the same time, the other young prodigies began laughing loudly as well.

“Pfft, ha-ha-ha! I almost died trying to hold that in.”

“Ha-ha-ha! They don’t know the first thing about martial arts, and they’re talking about the Ten Dragons and Phoenixes?”

How long did they laugh?

When they finally managed to stop, what they saw was one person staring quietly up at them.

“Finished laughing?”

At the ‘young master’s’ words, the young prodigies froze.

They had all been raised precious and pampered. How long had it been since anyone had spoken down to them like that?

The chilly silence was broken by Woo Jintae’s dry voice.

“And if we have?”

The ‘young master’ smiled brightly.

“Get down here right now, you fucking sons of bitches. My neck hurts.”

* * *

Hyuk Mujin asked with an expectant look in his eyes,

“Are you going to fight them?”

“Depends on what they do.”

“Once you’ve called them fucking sons of bitches, isn’t that asking for a fight?”

“That would be fine, too. Also, can you see all the spit those bastards sprayed on my face?”

“You’re completely drenched.”

Hyuk Mujin briskly wiped my face with his sleeve.

“What if they don’t apologize?”

“They ought to.”

“Look at their faces. They’re never going to apologize.”

“Then they can get the shit beaten out of them.”

“There are women among them, too…”

“I believe in gender equality.”

“What?”

“I beat everyone equally.”

Cheongpung, who had been watching blankly, looked at me with sparkling eyes.

“Oh. I don’t really understand, but it sounds cool.”

“It’s nothing special… Anyway, thanks.”

Even if I wanted to say more, I was no longer given the time.

The five bastards—or rather, the five sons and daughters of bitches—had jumped down from the second floor.

*Tap.*

They landed lightly, as befitted First Rate masters. One person stepped forward from among the five as they glared at us.

Level 45. He was tall and good-looking. He was also the one who had laughed first.

“I…”

“Are you the head?”

“The head?”

“Are you the boss of the five of you?”

The man gave a short laugh.

“You’d better watch your mouth. If you knew who the people here were, including me…”

I smiled back and scanned through their Level windows.

“Seongryong, Cheonwoo, Myeonghwa, Sohye, and finally, you—Jintae. Want me to tell you your family names, too?”

“…”

“…”

Five pairs of astonished eyes turned toward me. No—along with Hyuk Mujin and Cheongpung, there were seven pairs of eyes fixed on me.

“Oh, and this is a personal request, but please don’t ask how I knew. I’m sick of that line. If you ask, I’ll hit you.”

“How did you…?”

“Did you stick radishes in your ears?”

The next moment, my palm struck the man’s cheek.

*Smack!*
```
