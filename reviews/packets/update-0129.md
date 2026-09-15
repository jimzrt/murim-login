<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0129.txt",
      "sha256": "1d3c152520d6122a055fe6c704e5e18d6118481c08a7d6b51bb4f6352bd1864f",
      "bytes": 13882
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "429d9be3a93e819d5609a6ff10a78ef4ca2886839e2977499f8fea9980f62e94",
      "bytes": 6280
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1a513174052371e0053a7bc74431ed7df05126f01a9dc56001c698da2f41b08b",
      "bytes": 22918
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "9e2c327fcb97d2e70b7144ceb56c02b2a38709c04695495b21ed73063c8ad61b",
      "bytes": 5199
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "e578238ee7ccd1f42113feff7a53ff2c1402c1c29f45d8e2adc5c0d593a6c2ec",
      "bytes": 1511
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "6da233461cd133caf3bab65dbc9c8204d7183ed7335d5d17c2f3d9e8e636dc2b",
      "bytes": 24583
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "f4947b74e1c433511b1d87698058a30f7eaf9fa77b961464a325c21cdc80071f",
      "bytes": 8154
    },
    {
      "path": "characters/Lee Cheonbaek.md",
      "sha256": "1d3b40b5afebdb113352e3491f2407621babf68dd33f332fb502024b4dcabcd3",
      "bytes": 3231
    },
    {
      "path": "characters/Wipeng.md",
      "sha256": "56e66e964c7000a45df8c230402b16ca9f8714187b6ed8e3b7bfb59255439eee",
      "bytes": 4621
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ed89bfefac4a198673026986a1fb836b08880b2a0cc2a198d07a219ae11558e5",
      "bytes": 19320
    }
  ],
  "estimated_tokens": 22100
}
-->

# Durable State Update — Chapter 129

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 129. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 129. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 129,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 129,
    "continuity_sources": [129],
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
    "The Lower District Sect sent a relief force with physicians, cooks, and laborers after the battle.",
    "Wolhwa's real name is Eun Sowol, and she is the Lower District Sect's Shanxi Branch Leader with authority over more than thirty Shanxi branches.",
    "Lee Seowol accepted Jin Wikyung's invitation to the Jin Family of Taiyuan's New Year gathering and offered the Mount Heng Sword Sect's territorial rights to the Jin Family as an apology.",
    "Lee Seowol proposed marriage to Jin Taekyung in exchange for the Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist; Taekyung decided to reject the proposal because of her age and because he loves Song Song.",
    "Forty-seven mounted bandits survived the battle, but the Lower District Sect can save only about thirty with its available medicine; the sect is spreading a rumor that the two Jin brothers defeated Pung Yang and rescued Mount Heng.",
    "Cheol Mubaek and Lee Cheonbaek first met more than thirty years ago, fought, and became close friends; Cheol is the ninth-generation successor of the Shura Annihilating Fist.",
    "Jopil is dead and left behind the Supreme Peak martial art Flame Divine Palm; the Fire King is a Supreme Peak master and the Fire Gate Clan has a single successor, but his current status is unknown.",
    "The Mount Heng Sword Sect formally apologized for Lee Cheonbaek's crimes, but Taekyung refused the apology and directed responsibility toward the Jin Family of Taiyuan.",
    "The Temporary Strength Pill is stored in Taekyung's Inventory and has been revealed to Jin Wikyung, Jin Mukyung, and Wipeng; its System description identifies Dark Heaven as its manufacturer and records its unknown Grade, Peak restriction, temporary power increase, +100 combat stats, fifteen years of internal energy, and Body-Protecting Qi effect.",
    "Jin Wikyung and Wipeng traveled to Sakju with fifty elite guards after receiving an emergency report about Pung Yang, the Red Wind Band, the Mount Heng Sword Sect, and the Jin brothers.",
    "The Jin Family of Taiyuan displayed a huge Sakju banner celebrating the safe return of Mukyung, Taekyung, and Hyuk Mujin.",
    "Taekyung, Mukyung, Wikyung, and Wipeng drank through the night for three days; Wipeng is called the God of Drinking and Taekyung is rumored to be the Night King.",
    "The Jin Family of Taiyuan arrived at a village in a procession of fifty mounted riders and received loud public acclaim for the family, Jin Taekyung, and Jin Mukyung.",
    "Taekyung's Sleeping Dragon of Shanxi Title effect strengthened to all stats +15 and Fame +200; his current Status Window shows Level 61, Fame 2,100 (+250), and 60 remaining points.",
    "Hyuk Mujin and Taekyung publicly exaggerated the battle's death toll and achievements, and the county magistrate and assembled crowd reacted with awe.",
    "The county magistrate delivered a City Lord's invitation to Taekyung for a gathering with several young prodigies, causing the System to create a Quest."
  ],
  "continuity_sources": [
    128
  ],
  "open_questions": [
    "How will the Jin Family of Taiyuan respond to Lee Seowol's proposed transaction and territorial transfer?",
    "Can Lee Seowol preserve or rebuild the Mount Heng Sword Sect with so few survivors?",
    "What are the Temporary Strength Pill's exact price and long-term aftereffect, and is it related to the Demonic Cult's Blood-Exploding Pill?",
    "What is Dark Heaven, and why do Jin Wikyung and Wipeng refuse to discuss it?",
    "What consequences will Pung Yang's death have for the Red Wind Band and the wider Murim?",
    "Is the Fire King still alive, and if so, where is he?",
    "Was Jopil truly the nineteenth-generation successor of the Flame Divine Palm, and how did he acquire it?",
    "What will result from the City Lord's invitation and the newly created Quest?"
  ],
  "safe_through": 128,
  "temporary_decisions": [
    "Render 잠력단 as Temporary Strength Pill and 폭혈단 as Blood-Exploding Pill.",
    "Render 만년한철 as Ten-Thousand-Year Cold Iron and 이름 없는 검 as Unnamed Sword.",
    "Render 열화신단 as Blazing Flame Divine Pill and 반 갑자 as half a jiazi, clarified as thirty years.",
    "Render 완전 회복 as Full Recovery and 회광반조 as final rally in this death-and-recovery context.",
    "Render 운칠기삼 as seven parts luck and three parts skill, and 운구기일 as nine parts luck and one part qi, with a footnote explaining the variation.",
    "Render 은공 as Benefactor, 절정 무공 as Peak martial arts, 급식 as school lunch, 고딩 as high schooler, 철컹 as clank, 산서성 as Shanxi Province, 총지부장 as Chief Branch Leader, 원단 as New Year's Day, 갑자 as jiazi, and 시진 as shichen.",
    "Render 일인전승 as single successor, 비인부전 as transmission only to the worthy, 구 대 계승자 as ninth-generation successor, 천하십대권법 as the ten greatest fist techniques in the world, 열화문 as Fire Gate Clan, 화왕 as Fire King, 삼성 as Three Saints, 십왕 as Ten Kings, 진무보법 as Jin Family's Manoeuvre Technique, 아이템창 as Item Window, 전서응 as messenger eagle, 고원 as Gaoyuan, 구주 as Nine Provinces, 사술 as dark arts, 마기 as demonic qi, 선천지기 as innate qi, 소음인 as Soeumin, 태양인 as Taeyangin, 암천 as Dark Heaven, 주신 as God of Drinking, 야왕 as Night King, 화주 as fire liquor, 화북 as North China, 현령 as county magistrate, 성주 as City Lord, 장 노인 as Old Man Jang, 적토마 as Red Hare, and 여포 as Lü Bu."
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

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 삼류     | **Third Rate**    |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 마적     | **mounted bandits**                              |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 시스템              | **System**                     |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 귀가      | **your family**                                                 |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 삭주 | **Sakju** | Jin Family branch location |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 봉황객잔 | **Phoenix Inn** | Famous Shanxi inn with luxurious lodging, imperial-court cuisine, and a beautiful proprietress. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 현령 | **county magistrate** | County official who greets Jin Taekyung and delivers the City Lord's invitation. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 128
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a tenant-farmer family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion; stationed outside Jin Taekyung’s pavilion while Taekyung recovers
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 128
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman who won the visible exchange with Pung Yang, was then incapacitated by five concealed throwing knives, and survived the battle to recover after Taekyung's intervention; recovered enough from his Internal Injuries to return to the Jin Family of Taiyuan, though he is not yet fully recovered
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 128
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm who now possesses forty-five years of internal energy with the Scorching Yang Qi attribute after fully absorbing the Blazing Flame Divine Pill; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius; possesses one Temporary Strength Pill in his Inventory and has reserved it for a worst-case, life-threatening contingency; Level 61 with 2,100 Fame and 60 unspent stat points, and the Sleeping Dragon of Shanxi Title now grants all stats +15 and Fame +200
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; loves Song Song; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect, whose marriage proposal he has decided to reject

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 128
- **Aliases:** Junzi Sword
- **Role:** Thirty-five-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan; preparing to consolidate Shanxi Murim under the family's leadership
- **Personality:** Calm and authoritative in public; affectionate and protective toward Taekyung beneath a stern mask; accepts responsibility from his subordinates and shows immediate concern for family
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate with Taekyung
- **Relationships:** Taekyung’s eldest brother and future Family Head; head of Wipeng; member of the Jin Family

### Lee Cheonbaek.md

# Lee Cheonbaek (이천백)

- **Safe through:** Chapter 125
- **Aliases:** Blood Wolf Sword
- **Role:** Former Sect Leader of the Mount Heng Sword Sect, killed during the Red Wind Band’s assault; father of Lee Seogeun and Lee Seowol
- **Personality:** Grief-stricken, resolute, and fiercely vengeful
- **Voice:** Quietly mournful when addressing his son; firm and uncompromising when declaring revenge
- **Relationships:** Deceased father of Lee Seogeun and Lee Seowol; also father of a deceased Young Sect Leader; former leader of the Mount Heng Sword Sect; longtime close friend and peer of Cheol Mubaek

### Wipeng.md

# Wipeng (위팽)

- **Safe through:** Chapter 128
- **Aliases:** Ghost Sword; God of Drinking
- **Role:** Jin Wikyung’s personal guard and commander of the thirty-elite pursuit team sent south under an assassin-hunt pretext
- **Personality:** Loyal, observant, teasing, and resigned to his master’s impulsive departures
- **Voice:** Weary and knowing; jokes with Jin Wikyung and uses Sound Transmission
- **Relationships:** Trusted guard and retainer of Jin Wikyung

## Korean source

```text
＃129화



띠링.



- 퀘스트가 생성되었습니다.



퀘스트



[성주의 초청]

높은 명성을 가진 이에게는 관심이 뒤따르기 마련.

산서잠룡에 관한 소문을 들은 산서성의 성주(城主)가 당신을 내일 있을 후기지수들과의 오찬에 초청합니다.



등급 : 삼류

제한 : 진태경

임무 : 성주가 주최하는 오찬에 참석 (미완료)

보상 : 성주의 반응에 따라 달라집니다.

실패 : 성주가 무척 우울해합니다.



퀘스트를 수락하시겠습니까?

Y   /   N

※ 퀘스트 거절 시, 성주가 삐질 수 있습니다.



‘성주가 나를?’

분명 뜻밖이지만 그리 놀랍지는 않다. 누군가의 유명세는 종종 정치인들에게 이용되기 마련이니까.

물론 미디어의 파급력이 거의 없는 세상이니만큼 개인적인 호기심이 더 크긴 할 것이다.

그런데…….

‘퀘스트를 거절하면 삐지는 건 또 뭐야.’

삐지긴 뭘 삐져. 턱살이 다섯 겹 정도 접힌 아저씨가 삐지는 광경을 상상하니 전신에 소름이 돋는다.

“소협?”

현령의 의아한 표정을 못 본 척하며 턱을 긁적였다.

‘음. 귀찮은데.’

고작해야 삼류 등급의 퀘스트. 얻을 수 있는 경험치나 명성도 적을 것이고 보상은 성주 비위를 살살 맞춰 줘야 얻을 수 있다.

그러느니 그 시간에 차라리 무공 수련을 하는 게 낫지 않을까.

‘내가 뭐, 성주가 부르면 냉큼 달려가야 하는 사람도 아니고.’

목숨을 잃을 뻔한 전투를 마치고 복귀하는 길인데, 당장 내일 얼굴도 모르는 성주라는 아저씨와 점심을 먹고 싶진 않다.

퀘스트를 거절해도 삐지는 걸로 끝날 텐데, 뭘. 많이 삐져라.

내가 최대한 정중하게 거절하려던 그때였다.

덥석.

“가겠습니다. 무조건!”

불쑥 나서서 초청장을 잡은 혁무진의 모습에 현령이 눈살을 찌푸렸다.

“그대를 초청하는 것이 아닐 텐데?”

방금과 다르게 싸늘한 목소리. 하지만 혁무진이 아랑곳하지 않고 넉살 좋게 웃어 보였다.

“아이고, 당연합죠. 다만 저희 공자님께서 평소 성주님을 워낙 존경해 온 터라 감격하셨는지 말을 못 하시기에.”

현령이 게슴츠레한 눈으로 나를 응시했다.

“흠, 사실이오?”

당연히 아니지.

그렇게 대답하려던 찰나, 현령을 등지고 돌아선 혁무진이 내게 입을 벙긋거렸다.

‘무조건 가라고?’

평소와는 다르게 어쩐지 필사적인 모습이다.

나는 빠르게 판단을 내렸다.

“물론입니다. 산서 사람 중에 성주님을 존경하지 않는 이가 어디 있겠습니까?”

“허허, 과연 대국(大國)의 백성답구려. 성주님께서 들으시면 아주 좋아하실 거요.”

그제야 얼굴을 펴고 흐뭇하게 웃은 현령이 돌아섰다.

“그럼 승낙한 것으로 알고 이만 가 보겠소. 진 소가주님과 진천검에게도 안부 전해 주시오.”

“아, 물론이죠.”

띠링.



- [성주의 초청] 퀘스트를 수락했습니다!



시스템 알림이 울렸다. 이젠 취소도 못 하겠네.

현령을 위시한 관군들이 멀어지자, 나는 혁무진을 꾹 밟으며 속삭였다.

“나한테 할 말이 있을 것 같은데, 응?”

“설명드릴게요. 일단 여기부터 빠져나간 후에.”

아직 주위에 지켜보는 눈이 너무 많다. 우리는 사람들의 환호 속에서 다시 말에 올랐다.

마을 안쪽으로 더 들어가 목적지에 도착하니 꼬마 점소이가 총알처럼 튀어나와 허리를 굽혔다.

“어서 옵쇼…… 헉.”

녀석은 오십 기의 기마, 호위대의 위압감에 한 번 놀라고 나와 혁무진을 보고 두 번 놀랐다.

며칠 전에 본 적이 있는, 봉황객잔의 점소이다.

“별채가 하룻밤에 은자 오십 냥. 맞지?”

“어어, 그때 그?”

“어허, 이놈이 하늘 같은 손님한테 삿대질을 해?”

준엄한 목소리로 점소이를 꾸짖은 혁무진이 묵직한 전낭을 던졌다.

꼬마는 우리의 눈치를 보다가 전낭에 가득한 은자를 보고 헛숨을 들이켰다.

“헛. 이, 이렇게 많이요?”

“지금부터 봉황객잔은 태원진가가 접수한다.”

“……너 쌍칼이니?”

누가 보면 조직 폭력배인 줄 알겠다.



* * *



마차에서 내린 좀비 세 마리는 음식이 나오자마자 허겁지겁 국물부터 들이켰다.

자그마치 사흘 동안 하루도 쉬지 않고 과음을 했으니 저럴 만도 하다. 아니, 무공을 익히지 않았다면 첫날에 바로 주독(酒毒)으로 죽었을지도 모르겠다.

“크허어어, 이제 좀 살겠네.”

해장을 끝낸 진위경이 의자에 몸을 기대자마자 위팽의 잔소리가 날아들었다.

“주군, 체통을 지키십시오. 체통을.”

“뭐 어떤가, 어차피 우리밖에 없는데.”

“그래도 자꾸 이런 모습을 보이시면 수하들이 어찌 생각하겠습니까?”

“괜찮네. 난 토하진 않았거든.”

단 한 마디로 위팽의 입을 닥치게 만든 진위경이 이번엔 내게 물었다.

“그래, 현령이 다녀갔다고?”

“네, 성주가 내일 오찬에 초청한다고 그러더라고요.”

“성주가?”

“왠지는 모르겠는데 저한테 관심이 있던데요. 거절할 생각이었는데 어떤 생각 없는 놈이 냉큼 받아 버리는 바람에.”

“그랬느냐? 도대체 누가?”

탁자 구석에서 눈치만 살피고 있던 혁무진이 쥐방울만 한 목소리로 대답했다.

“접니다, 소가주님.”

“아하, 우리 막내 오른팔이라는 그 친구구먼. 얼마 전까지 수문각에 있던. 자네 이름이 아마…… 혁무진이었던가?”

현대와 비교하자면 태원진가는 재벌 기업이고 진위경은 회장의 장남이자 실질적인 경영자다.

맨날 성질 더러운 상사 밑에서 구박만 받던 혁 대리가 감격한 목소리로 대답했다.

“아, 알아봐 주셔서 감사합니다.”

“오히려 내가 감사하지. 우리 막내가 아직 서투른 구석이 있으니 오늘처럼 잘 도와주게.”

“조, 존명!”

“하하, 씩씩해서 보기 좋군.”

유쾌하게 웃은 진위경이 내게 고개를 돌렸다.

“성주의 초청을 받아들인 건 백번 잘한 일이다.”

“그런가요? 제가 지금까지 겪어 본 바로는 그쪽은 무림과 별 관계도 없어 보이던데.”

“오래전부터 관(官)과 무림은 불가침의 관계다. 알고 있느냐?”

“네, 어느 정도는.”

무림을 소설로 배운 나다. 무협 소설에서 자주 쓰이는 설정은 이곳, 무림에서도 별반 다르지 않았다.

“서로의 영역을 인정하지만, 관의 심기를 거슬리게 해서 좋을 것이 없다. 무림은 천하의 일부일 뿐, 천하가 무림인 것이 아니니까.”

진위경이 앞에 놓인 그릇을 가리켰다. 반쯤 차 있는 국물과 커다란 고기 한 덩어리가 보인다.

“무슨 말인지 알겠느냐?”

나는 고개를 끄덕였다.

그릇은 천하, 무림은 그 안에 들어있는 고깃덩어리다.

“우리는 무림인이지만 천하를 다스리는 것은 황제다. 백성들 사이에서 천자(天子)의 권위는 절대적이야. 바로 그 황제의 명을 받들어 각 성을 다스리는 자가 성주이니 상당한 힘과 권한이 있지.”

“우리 태원진가 이상으로요?”

“권한만 보면 그렇다. 그저 서로의 세력을 인정하고 존중하는 것이지. 무림 문파는 관이 해결할 수 없는 치안을 맡기도 하고, 관군에 무공 교두를 파견하기도 한다. 관에서는 그에 상응하는 도움을 주면서 상부상조하고 있다.”

관과 무림은 악어와 악어새의 관계라는 말이군.

잠시 생각하던 나는 아까부터 자꾸만 들던 의문을 입 밖으로 꺼냈다.

“그런데 왜 마적들이 개판 치고, 문파끼리 대규모 전투가 벌어질 때도 가만히 있는 겁니까? 지난번 전쟁 때야 무림인끼리의 일이니 가만히 있었다 쳐도, 마적 놈들은 아니잖아요?”

이천백도 삭주지부를 몰살시키고 아이들을 죽이는 미친 짓거리를 하긴 했지만, 어쨌든 피해자들은 태원진가 소속이었다.

엄연히 말하면 무림 문파 간의 은원(恩怨)에 희생된 이들이라 할 수 있겠다.

하지만 마적 놈들은 그런 거 없이 닥치는 대로 죽이고 불태우는 놈들 아닌가?

‘마적 입장에서는 만만한 게 양민이니까.’

강자에게 약하고, 약자에게 강한 놈들이 바로 마적이다.

아무튼 중요한 건 항산검문으로 가던 길에 마주친 마적들만 수십 명인데, 관군은 구경도 못 해 봤다는 거다.

“그건…….”

진위경이 말꼬리를 흐리자, 조용히 음식만 흡입하던 진무경이 툭 내뱉었다.

“성주가 무능해서지. 아니, 이 경우는 황제가 무능한 건가?”

말이 끝나는 순간 혁무진은 경기를 일으켰고, 진위경과 위팽은 짐짓 얼굴을 굳혔다.

“어허, 무경아.”

“어차피 우리뿐이라 엿들을 사람도 없습니다. 제가 틀린 말 한 것도 아니고요.”

“이공자, 본 가는 아직 구파일방도, 오대세가도 되지 못합니다. 자칫 문제가 생길 말은 삼가십시오.”

나는 마지못해 고개를 끄덕이는 진무경에게 물었다.

“성주가 무능하다는 게 무슨 소리지?”

“무능이라는 단어를 모르나?”

“확 그냥, 황제 욕했다고 관아에 고발해 버릴까.”

“역모죄는 최소 삼족(三族)이 처벌받지. 축하한다, 아우야.”

진무경 이 자식, 말발이 제법 늘었는데.

“지금 성주가 누구인지 알고 있나?”

“김춘배?”

“……모르면 모른다고 해라.”

나를 벌레 보듯 바라본 녀석이 다시 입을 열었다.

“현 산서 성주는 주씨 성을 쓴다.”

“그래서?”

“그래서라니? 황족이란 말이다. 황족!”

“아, 그래?”

주씨 왕조였던 모양이다. 한순간에 황제 성씨도 모르는 무식한 놈으로 낙인찍혔지만.

그래도 뭐, 이런 일이 한두 번이 아니라 이제는 별로 부끄럽지도 않다.

“알겠으니까 계속해.”

한숨을 푹 내쉰 진무경이 말을 이었다.

“지금의 성주는 황상의 막내아우로, 황실 관직으로는 친왕(親王)이다. 황실의 직계이니 성주들과는 격이 달라. 억지로라도 초청에 응해서 체면을 세워 줘야 하는 인물이지.”

“오오.”

확실히 격이 다르긴 하다. 그냥 성주가 아니라 황제의 아우. 무려 진짜 왕.

천자의 아들로 태어나 천자의 동생이 되었으니 금수저 정도가 아니라 비브라늄 수저라고 할 수 있겠다.

현대에 있는 북한의 핵수저, 그 이상.

“그런데 왕씩이나 되는 양반이 왜 그렇게 무능해? 형한테 편지 한 통 쓰면 위에서 지원 빵빵하게 해 주겠구먼. 둘이 사이 안 좋나?”

“글쎄, 그 집안 사정이야 정확히는 모르지만, 딱히 우애가 좋을 것 같지는 않군. 현 황제도 바로 위의 형인 태자를 암살하고 황위에 올랐다는 소문이 도니까.”

“권력욕 보소.”

“만두 하나에 살인도 일어나는데, 황위는 오죽할까.”

진위경과 위팽은 입을 딱 벌렸고, 혁무진은 다시 한번 경기를 일으켰다.

“판관님, 저는 아무것도 듣지 못했습니다. 정말 아무것도 모릅니다. 사실 이미 오래전부터 귀가 들리지 않습니다…….”

미친놈처럼 중얼거리는 혁무진의 뒤통수를 후려치는 진무경을 향해 내가 물었다.

“황제랑 사이가 안 좋아서 지원을 안 해 주는 건가? 아니면 그냥 술과 여자에 빠져서?”

“술? 여자?”

녀석이 또 피식 웃었다.

“이제 겨우 열 살이다. 주지육림에 빠지기에는 너무 이른 나이지.”

“뭐, 열 살? 열 살짜리가 성주란 말이야?”

“황실 직계니까. 성주가 아니라 그 이상도 될 수 있는 핏줄이야.”

문득 아까 봤던 시스템 메시지가 생각난다.



※ 퀘스트 거절 시, 성주가 삐질 수 있습니다.



나이도 먹을 만큼 먹은 아저씨가 주책이다 싶었는데, 열 살짜리 어린애라니 이제야 납득이 간다.

떨어지는 낙엽에도 삐질 나이 아닌가?

“더 재밌는 사실은 처음 성주로 부임했던 게 오 년 전이라는 거지.”

“……다섯 살? 미쳤군.”

다섯 살짜리가 뭘 알겠나. 산서성 치안이 개판이 된 이유도 대충 짐작이 간다. 진무경이 왜 성주가 아니라 황제가 더 무능한 거라고 했는지도.

동네 구멍가게도 아니고, 능력과 책임감이 필요한 막중한 자리에 어린아이를 앉혀 놨으니 제대로 돌아갈 리 만무하지.

“그런데 어떻게 그렇게 잘 알아?”

무공에만 미쳐 있던 진무경이 정세에 제법 빠삭한 것이 신기해서 물어본 건데, 뜻밖의 대답이 돌아왔다.

“직접 만난 적이 있으니까. 불려갔다고 해야 맞겠군.”

“어, 진짜?”

“삼 년 전이었지.”

하긴, 내가 근래 들어 떠오르는 슈퍼 루키라면 진무경은 이미 입지를 다진 절정 고수다. 나보다 앞서 초청을 받는 게 당연했다.

“어땠어?”

진무경이 묘한 눈빛으로 나를 바라봤다.

그러더니 웃음과 빡침이 뒤섞인, 보는 것만으로도 불길해지는 표정으로 말한다.

“개 같았다.”
```

## Final English reading copy

```markdown
# Chapter 129

Ding.

> **System**
>
> A **Quest** has been created.
>
> **Quest**
>
> **The City Lord’s Invitation**
>
> High renown is bound to attract attention.
>
> The City Lord of Shanxi Province, having heard rumors about the Sleeping Dragon of Shanxi, invites you to a luncheon with several young prodigies tomorrow.
>
> **Grade:** Third Rate
>
> **Restriction:** Jin Taekyung
>
> **Objective:** Attend the luncheon hosted by the City Lord (Incomplete)
>
> **Reward:** Varies according to the City Lord’s reaction.
>
> **Failure:** The City Lord becomes extremely depressed.
>
> Would you like to accept the Quest?
>
> **Y / N**
>
> ※ If you reject the Quest, the City Lord may sulk.

*The City Lord wants me?*

It was certainly unexpected, but not all that surprising. A person’s fame was often used by politicians, after all.

Of course, this was a world where media had almost no reach, so personal curiosity was probably the greater factor.

But…

*What do you mean, the City Lord might sulk if I reject the Quest?*

What was there to sulk about? The thought of a five-chin-folded middle-aged man sulking sent goose bumps all over my body.

“Young Hero?”

Pretending not to notice the county magistrate’s puzzled expression, I scratched my chin.

*Hmm. What a pain.*

It was only a Third Rate Quest. The EXP and Fame I could gain would probably be minimal, and I’d have to carefully flatter the City Lord to obtain the reward.

Wouldn’t it be better to spend that time practicing martial arts instead?

*It’s not like I’m someone who has to come running the instant the City Lord calls.*

I was on my way back after a battle in which I had nearly lost my life. I didn’t particularly want to have lunch tomorrow with some middle-aged man called the City Lord whose face I had never even seen.

If I rejected the Quest, the worst that could happen was that he’d sulk. Whatever. He could sulk as much as he wanted.

I was just about to turn him down as politely as possible when—

Grab.

“We’ll go. Absolutely!”

Hyuk Mujin suddenly stepped forward and snatched the invitation. The county magistrate frowned.

“I don’t believe I invited you.”

His voice was cold, unlike before. Hyuk Mujin didn’t care in the slightest. He simply flashed a shameless smile.

“Oh my, of course you didn’t. It’s just that our Young Master has always respected the City Lord so deeply that he was too moved to speak.”

The county magistrate stared at me through narrowed eyes.

“Hmm. Is that true?”

Of course it wasn’t.

I was about to say so when Hyuk Mujin, having turned his back to the county magistrate, silently mouthed at me.

*You absolutely have to go?*

Unlike usual, he looked strangely desperate.

I made a quick decision.

“Of course. Is there anyone in Shanxi who doesn’t respect the City Lord?”

“Ha-ha, truly the words of a citizen of a great nation. The City Lord will be delighted to hear that.”

Only then did the county magistrate relax his face and smile with satisfaction. He turned around.

“Then I’ll consider it accepted and take my leave. Please convey my regards to the Lesser Family Head and the Heaven Shaking Sword.”

“Ah, of course.”

Ding.

> **System**
>
> You have accepted the **The City Lord’s Invitation** Quest!

The System notification rang out.

*Now I can’t even cancel it.*

Once the county magistrate and the government troops had moved away, I whispered as I pressed my foot down on Hyuk Mujin’s.

“I think you have something to tell me, don’t you?”

“I’ll explain. First, let’s get out of here.”

There were still too many eyes watching us. Amid the people’s cheers, we mounted our horses again.

We proceeded farther into the village and reached our destination. A little errand boy shot out like a bullet and bowed at the waist.

“Welcome—gasp.”

He was startled once by the fifty mounted riders and the intimidating presence of the escort, then a second time when he recognized Hyuk Mujin and me.

He was the errand boy from the Phoenix Inn. I had seen him a few days ago.

“The private annex is fifty nyang of silver for one night. That’s right, isn’t it?”

“Uh, you’re the one from back then?”

“Hey, you little brat. Are you pointing at a guest as lofty as the heavens?”

After scolding the boy in a stern voice, Hyuk Mujin tossed him a heavy money pouch.

The little boy glanced nervously between us, then inhaled sharply when he saw the pouch packed with silver.

“Gasp. Th-this much?”

“From this moment on, the Phoenix Inn is under the control of the Jin Family of Taiyuan.”

“…Are you some kind of two-knife gangster?”

Anyone watching would have thought we were members of organized crime.

* * *

The three zombies climbed out of the carriage and began gulping down the broth the moment the food arrived.

It was understandable, considering they had spent three days drinking to excess without taking a single day off. No—if they hadn’t practiced martial arts, they might have died of alcohol poisoning on the first day.

“Guhhh, I feel alive again.”

The instant Jin Wikyung leaned back in his chair after finishing his hangover cure, Wipeng’s nagging flew at him.

“My lord, please maintain your dignity. Your dignity.”

“What does it matter? We’re the only ones here.”

“Even so, what will your subordinates think if you keep showing them this side of yourself?”

“It’s fine. I didn’t throw up.”

With a single sentence, Jin Wikyung silenced Wipeng. Then he turned to me.

“So, the county magistrate came by?”

“Yes. He said the City Lord was inviting me to a luncheon tomorrow.”

“The City Lord?”

“I don’t know why, but he seemed interested in me. I was planning to reject it, but some thoughtless idiot accepted it without hesitation.”

“Did he? Who on earth would do that?”

Hyuk Mujin, who had been sitting in the corner of the table and nervously watching our expressions, answered in a tiny voice.

“That would be me, Lesser Family Head.”

“Ah, I see. You’re the fellow who’s supposed to be our youngest brother’s right-hand man. The one who was in the Gatekeeper Pavilion until recently. Your name was… Hyuk Mujin, wasn’t it?”

Compared to the modern world, the Jin Family of Taiyuan was a conglomerate, while Jin Wikyung was the chairman’s eldest son and the actual head of the company.

Assistant Manager Hyuk, who had spent all his time being bullied under a foul-tempered boss, answered in a deeply moved voice.

“Ah, thank you for remembering me.”

“I should be thanking you. Our youngest brother still has some rough edges, so continue helping him as you did today.”

“A-as you command!”

“Ha-ha. It’s good to see such spirit.”

Jin Wikyung laughed cheerfully, then turned back to me.

“Accepting the City Lord’s invitation was absolutely the right thing to do.”

“Really? From what I’ve experienced so far, he doesn’t seem to have much to do with the Murim.”

“For a long time, the government and the Murim have maintained a relationship of noninterference. Do you know that?”

“Yes, more or less.”

I had learned about the Murim through novels. The common settings in martial-arts fiction weren’t all that different here in the Murim.

“They recognize each other’s domains, but there is nothing to be gained by offending the government. The Murim is merely one part of the world. The world is not the Murim.”

Jin Wikyung pointed toward the bowl in front of him. It contained half a bowl of broth and one large chunk of meat.

“Do you understand what I mean?”

I nodded.

The bowl was the world, and the chunk of meat inside it was the Murim.

“We are martial artists, but it is the Emperor who rules the world. Among the people, the authority of the Son of Heaven is absolute. The City Lords govern their respective provinces under the Emperor’s command, so they possess considerable power and authority.”

“More than the Jin Family of Taiyuan?”

“In terms of authority alone, yes. We simply recognize and respect each other’s power. Murim sects sometimes take responsibility for maintaining public order when the government cannot resolve a problem, and they also dispatch martial arts instructors to train government troops. The government offers assistance in return, so the two sides help each other.”

So the government and the Murim were like the crocodile and the crocodile bird.

After thinking for a moment, I finally voiced the question that had been bothering me since earlier.

“Then why do you sit back and do nothing when mounted bandits run wild or large-scale battles break out between sects? I can understand staying out of the last war because it was a matter between martial artists, but the mounted bandits are different, aren’t they?”

Lee Cheonbaek had massacred everyone at the Sakju Branch and committed the insane act of killing children, but the victims had belonged to the Jin Family of Taiyuan.

Strictly speaking, they could be considered people who had been sacrificed to the gratitude and grudges between Murim sects.

But the mounted bandits killed indiscriminately and burned everything in their path, didn’t they?

*From the mounted bandits’ perspective, commoners were easy prey.*

They were weak before the strong and strong before the weak. That was what mounted bandits were.

The important point was that I had encountered dozens of mounted bandits on the way to the Mount Heng Sword Sect, yet I hadn’t even seen a government soldier.

“That’s…”

Jin Wikyung let his voice trail off. Jin Mukyung, who had been silently inhaling his food until then, suddenly spoke.

“Because the City Lord is incompetent. No, in this case, is the Emperor incompetent?”

The moment he finished speaking, Hyuk Mujin had a fit, while Jin Wikyung and Wipeng deliberately hardened their expressions.

“Hey, Mukyung.”

“It’s just us here. No one can overhear us. And I haven’t said anything untrue.”

“Second Young Master, our family does not yet stand alongside the Nine Sects and One Gang or the Five Great Families. Please refrain from saying anything that could cause trouble.”

I asked Jin Mukyung, who reluctantly nodded.

“What do you mean, the City Lord is incompetent?”

“Do you not know the meaning of the word incompetent?”

“Should I report you to the authorities for insulting the Emperor?”

“Treason gets at least three clans punished. Congratulations, little brother.”

*This guy Jin Mukyung has gotten pretty good with words.*

“Do you know who the City Lord is right now?”

“Kim Chunbae?”

“…If you don’t know, just say you don’t know.”

He looked at me as if I were a bug, then continued.

“The current City Lord of Shanxi has the surname Zhu.”

“So?”

“What do you mean, ‘so’? He’s a member of the imperial family. The imperial family!”

“Oh, really?”

It seemed to be a Zhu dynasty. I had been branded an ignorant fool who didn’t even know the Emperor’s surname in the space of a moment.

Still, it wasn’t as if this sort of thing had only happened once or twice. I wasn’t even embarrassed anymore.

“Fine, I get it. Continue.”

Jin Mukyung sighed deeply and went on.

“The current City Lord is the Emperor’s youngest brother. His imperial title is a Prince. He is a direct member of the imperial family, so he stands on a different level from the other City Lords. He is someone whose invitation we must accept, even if only to preserve his dignity.”

“Oh.”

He really was on a different level. Not just an ordinary City Lord, but the Emperor’s brother. An actual king, no less.

Born the son of the Son of Heaven and then becoming the younger brother of the Son of Heaven, he wasn’t merely born with a silver spoon in his mouth. He had a vibranium spoon.

The North Korean nuclear spoon of the modern world—and then some.

“Then how can someone who’s practically a king be so incompetent? If he writes his brother a single letter, he could get all the support he needs from above. Are they on bad terms?”

“Who knows? I don’t know the details of that family’s circumstances, but they don’t seem particularly close. There are rumors that the current Emperor assassinated the Crown Prince, the brother immediately older than him, before ascending the throne.”

“Talk about a hunger for power.”

“People kill over a single dumpling. Imagine what they’d do for the imperial throne.”

Jin Wikyung and Wipeng’s mouths fell open, while Hyuk Mujin had another fit.

“Judge, I didn’t hear anything. I truly know nothing. In fact, I haven’t been able to hear for a long time…”

As Hyuk Mujin muttered like a madman, Jin Mukyung smacked him across the back of the head. I asked,

“Does he not receive support because he’s on bad terms with the Emperor? Or is he simply lost in alcohol and women?”

“Alcohol? Women?”

Jin Mukyung let out another quiet laugh.

“He’s only ten years old. It’s too early for him to lose himself in wine and women.”

“What, ten? You mean a ten-year-old is the City Lord?”

“He’s a direct member of the imperial family. He has the bloodline to become more than a City Lord.”

The System message I’d seen earlier suddenly came to mind.

> If you reject the Quest, the City Lord may sulk.

I had thought it was ridiculous for a middle-aged man to act so childish, but now that I knew he was a ten-year-old boy, it finally made sense.

Wasn’t that the age when you’d sulk at a falling leaf?

“The more amusing fact is that he was first appointed City Lord five years ago.”

“…Five years old? That’s insane.”

What could a five-year-old possibly know? I could roughly guess why the public order in Shanxi Province had become such a mess. I also understood why Jin Mukyung had said that the Emperor, rather than the City Lord, was more incompetent.

This wasn’t some neighborhood convenience store. They had put a child in a position that demanded ability and responsibility. There was no way things could run properly.

“How do you know all this?”

I asked because it was surprising that Jin Mukyung, who had been obsessed with martial arts and nothing else, was so well-informed about current affairs.

The answer I received was unexpected.

“Because I’ve met him before. More accurately, I was summoned.”

“Oh, really?”

“Three years ago.”

Well, if I was the rising super rookie of the moment, Jin Mukyung was already an established Peak master. It made sense that he would have been invited before me.

“What was he like?”

Jin Mukyung looked at me with a strange glint in his eyes.

Then, wearing an ominous expression that mixed laughter with irritation, he spoke.

“He was a fucking nightmare.”
```
